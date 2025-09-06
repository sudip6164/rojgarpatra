from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('create/', views.create_resume, name='create'),
    path('<uuid:resume_id>/', views.resume_detail, name='detail'),
    path('<uuid:resume_id>/edit/', views.edit_resume, name='edit'),
    path('<uuid:resume_id>/delete/', views.delete_resume, name='delete'),
    path('<uuid:resume_id>/preview/', views.preview_resume, name='preview'),
    path('<uuid:resume_id>/download/', views.download_pdf, name='download_pdf'),
]
