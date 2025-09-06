from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education, WorkExperience, ExtracurricularActivity, Certification, Project


class ResumeForm(forms.ModelForm):
    """Main resume form"""
    class Meta:
        model = Resume
        fields = [
            'title', 'full_name', 'email', 'phone', 'address',
            'linkedin_url', 'github_url', 'portfolio_url', 'skills'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Resume Title'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Phone Number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Address',
                'rows': 3
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'LinkedIn URL (optional)'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'GitHub URL (optional)'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Portfolio URL (optional)'
            }),
            'skills': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Enter skills separated by commas (e.g., Python, Django, JavaScript)',
                'rows': 3
            }),
        }


class EducationForm(forms.ModelForm):
    """Education form"""
    class Meta:
        model = Education
        fields = [
            'institution', 'degree', 'field_of_study', 'start_date', 
            'end_date', 'is_current', 'grade', 'description'
        ]
        widgets = {
            'institution': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Institution Name'
            }),
            'degree': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Degree (e.g., Bachelor of Science)'
            }),
            'field_of_study': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Field of Study (optional)'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'is_current': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
            }),
            'grade': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Grade/GPA (optional)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Description (optional)',
                'rows': 3
            }),
        }


class WorkExperienceForm(forms.ModelForm):
    """Work experience form"""
    class Meta:
        model = WorkExperience
        fields = [
            'company', 'position', 'location', 'start_date', 
            'end_date', 'is_current', 'description'
        ]
        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Company Name'
            }),
            'position': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Job Title/Position'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Location (optional)'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'is_current': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Job responsibilities and achievements',
                'rows': 4
            }),
        }


class ExtracurricularActivityForm(forms.ModelForm):
    """Extracurricular activity form"""
    class Meta:
        model = ExtracurricularActivity
        fields = [
            'title', 'organization', 'start_date', 
            'end_date', 'is_current', 'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Activity Title'
            }),
            'organization': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Organization (optional)'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'is_current': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Description of the activity',
                'rows': 3
            }),
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            'title', 'issuer', 'issue_date', 'expiration_date',
            'credential_id', 'credential_url', 'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Certification Title'}),
            'issuer': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Issuing Organization (optional)'}),
            'issue_date': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'type': 'date'}),
            'credential_id': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Credential ID (optional)'}),
            'credential_url': forms.URLInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Credential URL (optional)'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Description (optional)', 'rows': 3}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'role', 'link', 'start_date', 'end_date', 'description', 'technologies'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Project Name'}),
            'role': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Role (optional)'}),
            'link': forms.URLInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Project URL (optional)'}),
            'start_date': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Brief description (optional)', 'rows': 3}),
            'technologies': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500', 'placeholder': 'Technologies (comma-separated, optional)'}),
        }


# Formsets for dynamic forms
EducationFormSet = inlineformset_factory(
    Resume, Education, form=EducationForm, extra=0, can_delete=True
)

WorkExperienceFormSet = inlineformset_factory(
    Resume, WorkExperience, form=WorkExperienceForm, extra=0, can_delete=True
)

ExtracurricularActivityFormSet = inlineformset_factory(
    Resume, ExtracurricularActivity, form=ExtracurricularActivityForm, extra=0, can_delete=True
)

CertificationFormSet = inlineformset_factory(
    Resume, Certification, form=CertificationForm, extra=0, can_delete=True
)

ProjectFormSet = inlineformset_factory(
    Resume, Project, form=ProjectForm, extra=0, can_delete=True
)
