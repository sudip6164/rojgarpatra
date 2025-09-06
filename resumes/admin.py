from django.contrib import admin
from .models import Resume, Education, WorkExperience, ExtracurricularActivity


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0
    ordering = ['order', '-start_date']


class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0
    ordering = ['order', '-start_date']


class ExtracurricularActivityInline(admin.TabularInline):
    model = ExtracurricularActivity
    extra = 0
    ordering = ['order', '-start_date']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'full_name', 'user__email')
    readonly_fields = ('id', 'created_at', 'updated_at')
    inlines = [EducationInline, WorkExperienceInline, ExtracurricularActivityInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'user', 'title', 'created_at', 'updated_at')
        }),
        ('Personal Details', {
            'fields': ('full_name', 'email', 'phone', 'address')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url', 'portfolio_url')
        }),
        ('Skills', {
            'fields': ('skills',)
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'resume', 'start_date', 'end_date')
    list_filter = ('start_date', 'is_current')
    search_fields = ('degree', 'institution', 'resume__full_name')


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'resume', 'start_date', 'end_date')
    list_filter = ('start_date', 'is_current')
    search_fields = ('position', 'company', 'resume__full_name')


@admin.register(ExtracurricularActivity)
class ExtracurricularActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'resume', 'start_date', 'end_date')
    list_filter = ('start_date', 'is_current')
    search_fields = ('title', 'organization', 'resume__full_name')
