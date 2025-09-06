from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import HttpRequest
from .models import User, Profile
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
import uuid


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # User can login but email needs verification
            user.save()
            
            # Create profile
            Profile.objects.create(user=user)
            
            # Send verification email
            send_verification_email(request, user)
            
            messages.success(request, 'Registration successful! Please check your email to verify your account.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                if not user.is_email_verified:
                    messages.warning(request, 'Please verify your email address.')
                return redirect('core:dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')


@login_required
def profile(request):
    """User profile view"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})


def verify_email(request, token):
    """Email verification view"""
    try:
        user = User.objects.get(email_verification_token=token)
        user.is_email_verified = True
        user.email_verification_token = uuid.uuid4()  # Generate new token
        user.save()
        messages.success(request, 'Email verified successfully!')
        return redirect('accounts:login')
    except User.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
        return redirect('core:home')


@login_required
def resend_verification(request):
    """Resend email verification"""
    if request.user.is_email_verified:
        messages.info(request, 'Your email is already verified.')
    else:
        send_verification_email(request, request.user)
        messages.success(request, 'Verification email sent!')
    
    return redirect('core:dashboard')


def send_verification_email(request, user):
    """Send email verification email"""
    verification_url = request.build_absolute_uri(
        reverse('accounts:verify_email', kwargs={'token': user.email_verification_token})
    )
    
    subject = 'Verify your RojgarPatra account'
    message = f"""
    Hi {user.username},
    
    Thank you for registering with RojgarPatra!
    
    Please click the link below to verify your email address:
    {verification_url}
    
    If you didn't create this account, please ignore this email.
    
    Best regards,
    RojgarPatra Team
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
    except Exception:
        messages.warning(request, 'Verification email could not be sent. Please check email settings.')
