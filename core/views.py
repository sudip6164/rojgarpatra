from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resumes.models import Resume


def home(request):
    """Home page view"""
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    """User dashboard view"""
    resumes = Resume.objects.filter(user=request.user).order_by('-updated_at')
    
    # Get user profile for completion status
    profile = getattr(request.user, 'profile', None)
    
    context = {
        'resumes': resumes,
        'profile': profile,
    }
    return render(request, 'core/dashboard.html', context)


def privacy_policy(request):
    """Privacy policy page"""
    return render(request, 'core/privacy_policy.html')


def terms_conditions(request):
    """Terms and conditions page"""
    return render(request, 'core/terms_conditions.html')
