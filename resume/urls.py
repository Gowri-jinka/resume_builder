# resume/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('auth/', views.auth_view, name='auth'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    
    path('choose-template/', views.choose_template_view, name='choose_template'),
    path('edit-resume/<int:resume_id>/', views.edit_resume_dispatcher_view, name='edit_resume'),

    path('build/single-column/<int:resume_id>/', views.build_single_column_view, name='build_single_column'),
    
    path('delete-resume/<int:resume_id>/', views.delete_resume, name='delete_resume'),

    path('update-experience/<int:experience_id>/', views.update_experience, name='update_experience'),
    path('delete-experience/<int:experience_id>/', views.delete_experience, name='delete_experience'),
    path('update-education/<int:education_id>/', views.update_education, name='update_education'),
    path('delete-education/<int:education_id>/', views.delete_education, name='delete_education'),
    path('update-skill/<int:skill_id>/', views.update_skill, name='update_skill'),
    path('delete-skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('update-project/<int:project_id>/', views.update_project, name='update_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update-certification/<int:certification_id>/', views.update_certification, name='update_certification'),
    path('delete-certification/<int:certification_id>/', views.delete_certification, name='delete_certification'),
    path('update-achievement/<int:achievement_id>/', views.update_achievement, name='update_achievement'),
    path('delete-achievement/<int:achievement_id>/', views.delete_achievement, name='delete_achievement'),
]