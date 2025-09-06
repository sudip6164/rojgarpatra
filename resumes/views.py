from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import Resume
from .forms import (
    ResumeForm, EducationFormSet, WorkExperienceFormSet, 
    ExtracurricularActivityFormSet, CertificationFormSet, ProjectFormSet
)
from .utils import generate_pdf


@login_required
def create_resume(request):
    """Create a new resume"""
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        education_formset = EducationFormSet(request.POST)
        work_formset = WorkExperienceFormSet(request.POST)
        activity_formset = ExtracurricularActivityFormSet(request.POST)
        cert_formset = CertificationFormSet(request.POST)
        project_formset = ProjectFormSet(request.POST)
        
        if (
            form.is_valid() and
            education_formset.is_valid() and
            work_formset.is_valid() and
            activity_formset.is_valid() and
            cert_formset.is_valid() and
            project_formset.is_valid()
        ):
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            
            education_formset.instance = resume
            education_formset.save()
            
            work_formset.instance = resume
            work_formset.save()
            
            activity_formset.instance = resume
            activity_formset.save()
            
            cert_formset.instance = resume
            cert_formset.save()

            project_formset.instance = resume
            project_formset.save()
            
            messages.success(request, 'Resume created successfully!')
            return redirect('resumes:detail', resume_id=resume.id)
    else:
        form = ResumeForm()
        education_formset = EducationFormSet()
        work_formset = WorkExperienceFormSet()
        activity_formset = ExtracurricularActivityFormSet()
        cert_formset = CertificationFormSet()
        project_formset = ProjectFormSet()
    
    context = {
        'form': form,
        'education_formset': education_formset,
        'work_formset': work_formset,
        'activity_formset': activity_formset,
        'cert_formset': cert_formset,
        'project_formset': project_formset,
        'is_create': True,
    }
    return render(request, 'resumes/create_edit.html', context)


@login_required
def edit_resume(request, resume_id):
    """Edit an existing resume"""
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        education_formset = EducationFormSet(request.POST, instance=resume)
        work_formset = WorkExperienceFormSet(request.POST, instance=resume)
        activity_formset = ExtracurricularActivityFormSet(request.POST, instance=resume)
        cert_formset = CertificationFormSet(request.POST, instance=resume)
        project_formset = ProjectFormSet(request.POST, instance=resume)
        
        if (
            form.is_valid() and
            education_formset.is_valid() and
            work_formset.is_valid() and
            activity_formset.is_valid() and
            cert_formset.is_valid() and
            project_formset.is_valid()
        ):
            form.save()
            education_formset.save()
            work_formset.save()
            activity_formset.save()
            cert_formset.save()
            project_formset.save()
            
            messages.success(request, 'Resume updated successfully!')
            return redirect('resumes:detail', resume_id=resume.id)
    else:
        form = ResumeForm(instance=resume)
        education_formset = EducationFormSet(instance=resume)
        work_formset = WorkExperienceFormSet(instance=resume)
        activity_formset = ExtracurricularActivityFormSet(instance=resume)
        cert_formset = CertificationFormSet(instance=resume)
        project_formset = ProjectFormSet(instance=resume)
    
    context = {
        'form': form,
        'education_formset': education_formset,
        'work_formset': work_formset,
        'activity_formset': activity_formset,
        'cert_formset': cert_formset,
        'project_formset': project_formset,
        'resume': resume,
        'is_create': False,
    }
    return render(request, 'resumes/create_edit.html', context)


@login_required
def resume_detail(request, resume_id):
    """View resume details"""
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    context = {'resume': resume}
    return render(request, 'resumes/detail.html', context)


@login_required
def delete_resume(request, resume_id):
    """Delete a resume"""
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted successfully!')
        return redirect('core:dashboard')
    
    context = {'resume': resume}
    return render(request, 'resumes/delete.html', context)


@login_required
def preview_resume(request, resume_id):
    """Preview resume in PDF format"""
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    context = {'resume': resume}
    return render(request, 'resumes/preview.html', context)


@login_required
def download_pdf(request, resume_id):
    """Download resume as PDF"""
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    context = {
        'resume': resume,
    }
    
    # Generate filename
    filename = f"{resume.full_name.replace(' ', '_')}_Resume.pdf"
    
    # Generate and return PDF
    return generate_pdf('resumes/pdf_template.html', context, filename, request=request)
