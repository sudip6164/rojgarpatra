from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Resume(models.Model):
    """Main resume model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=200, default='My Resume')
    
    # Personal Information
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    
    # Skills
    skills = models.TextField(help_text="Enter skills separated by commas")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.title} - {self.full_name}"
    
    @property
    def skills_list(self):
        """Return skills as a list"""
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]


class Education(models.Model):
    """Education model"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"


class WorkExperience(models.Model):
    """Work experience model"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experience')
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class ExtracurricularActivity(models.Model):
    """Extracurricular activities model"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='extracurricular_activities')
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return self.title
