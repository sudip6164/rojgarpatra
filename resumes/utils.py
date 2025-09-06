from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from io import BytesIO
import os
try:
    from weasyprint import HTML as WP_HTML
except Exception:  # Missing native deps on Windows
    WP_HTML = None
try:
    from xhtml2pdf import pisa
except Exception:
    pisa = None
try:
    import pdfkit
except Exception:
    pdfkit = None


def _wkhtmltopdf_config():
    """Try to locate wkhtmltopdf binary and build a pdfkit configuration."""
    if pdfkit is None:
        return None
    # Explicit path via env var
    env_path = os.environ.get('WKHTMLTOPDF_PATH')
    if env_path and os.path.exists(env_path):
        try:
            return pdfkit.configuration(wkhtmltopdf=env_path)
        except Exception:
            pass
    # Common install paths (Windows and Linux)
    common_paths = [
        r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe",
        r"C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe",
        "/usr/local/bin/wkhtmltopdf",
        "/usr/bin/wkhtmltopdf",
    ]
    for path in common_paths:
        if os.path.exists(path):
            try:
                return pdfkit.configuration(wkhtmltopdf=path)
            except Exception:
                continue
    # Fallback to PATH
    try:
        return pdfkit.configuration()
    except Exception:
        return None


def _try_generate_with_wkhtmltopdf(html: str) -> bytes | None:
    if pdfkit is None:
        return None
    config = _wkhtmltopdf_config()
    if config is None:
        return None
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'disable-smart-shrinking': '',
        'print-media-type': '',
        'dpi': 96,
        'quiet': '',
        # Match browser zoom to avoid unexpected scaling
        'zoom': 1,
    }
    try:
        return pdfkit.from_string(html, False, options=options, configuration=config)
    except Exception:
        return None


def _try_generate_with_weasyprint(html: str, request=None) -> bytes | None:
    if WP_HTML is None:
        return None
    try:
        base_url = request.build_absolute_uri('/') if request else None
        return WP_HTML(string=html, base_url=base_url).write_pdf()
    except Exception:
        return None


def _try_generate_with_xhtml2pdf(html: str) -> bytes | None:
    if pisa is None:
        return None
    buffer = BytesIO()
    status = pisa.CreatePDF(html, dest=buffer, link_callback=link_callback)
    if status.err:
        return None
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


def generate_pdf(template_src, context_dict, filename, request=None):
    """
    Generate PDF from HTML template.
    Preference order (unless overridden by PDF_ENGINE):
    1) wkhtmltopdf (best HTML/CSS fidelity)
    2) WeasyPrint
    3) xhtml2pdf
    """
    template = get_template(template_src)
    html = template.render(context_dict)

    preferred = os.environ.get('PDF_ENGINE', '').lower()
    engines = []
    if preferred in ('wkhtmltopdf', 'weasyprint', 'xhtml2pdf'):
        engines.append(preferred)
    # Always ensure we try all engines in sensible order
    for e in ('wkhtmltopdf', 'weasyprint', 'xhtml2pdf'):
        if e not in engines:
            engines.append(e)

    pdf_bytes = None
    for engine in engines:
        if engine == 'wkhtmltopdf' and pdfkit is not None and pdf_bytes is None:
            pdf_bytes = _try_generate_with_wkhtmltopdf(html)
        elif engine == 'weasyprint' and WP_HTML is not None and pdf_bytes is None:
            pdf_bytes = _try_generate_with_weasyprint(html, request=request)
        elif engine == 'xhtml2pdf' and pisa is not None and pdf_bytes is None:
            pdf_bytes = _try_generate_with_xhtml2pdf(html)
        if pdf_bytes:
            break

    if not pdf_bytes:
        message = (
            'PDF generation failed. Please install wkhtmltopdf and ensure it\n'
            'is on your PATH, or set PDF_ENGINE to xhtml2pdf as a fallback.'
        )
        return HttpResponse(message, content_type='text/plain')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    response.write(pdf_bytes)
    return response


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """
    # Use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # Convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # Handle absolute uri (ie: http://some.tld/foo.png)

    # Make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path
