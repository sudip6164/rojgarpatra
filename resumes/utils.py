from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from io import BytesIO
import os
try:
    from xhtml2pdf import pisa
except Exception:
    pisa = None


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
    Generate PDF from HTML template using xhtml2pdf only.
    """
    template = get_template(template_src)
    html = template.render(context_dict)

    pdf_bytes = _try_generate_with_xhtml2pdf(html)
    if not pdf_bytes:
        return HttpResponse('PDF generation failed with xhtml2pdf.', content_type='text/plain')

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
