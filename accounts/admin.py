from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom user admin"""
    list_display = ('email', 'username', 'is_email_verified', 'is_staff', 'date_joined')
    list_filter = ('is_email_verified', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Email Verification', {'fields': ('is_email_verified', 'email_verification_token')}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('user', 'full_name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'first_name', 'last_name')
    ordering = ('-created_at',)
