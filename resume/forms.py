# resume/forms.py
from django import forms
from .models import (
    PersonalDetails, ProfessionalSummary, Experience, Education, Skill, 
    Project, Certification, Achievement
)

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        exclude = ('resume',)

class ProfessionalSummaryForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSummary
        fields = ['summary']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ('resume',)
        labels = {
            'job_title': 'Title (e.g., Software Engineer, Intern)',
            'company': 'Company / Organization',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'currently_work_here': 'I currently work here',
            'responsibilities': 'Key Responsibilities & Achievements',
            'is_internship': 'This is an internship',
        }
        widgets = {
            'responsibilities': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('resume',)
        labels = {
            'institution': 'Institution Name',
            'degree': 'Degree / Certificate',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('resume',)
        labels = {
            'category': 'Skill Category',
            'skills_list': 'Skills (comma-separated)',
        }
        widgets = {
            'skills_list': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Python, JavaScript, Django'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('resume',)
        labels = {
            'project_name': 'Project Name',
            'project_link': 'Project Link (Optional)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = ('resume',)
        labels = {
            'name': 'Certification Name',
            'issuing_organization': 'Issuing Organization',
            'date_issued': 'Date Issued',
            'credential_url': 'Credential Link (Optional)',
        }
        widgets = {
            'date_issued': forms.DateInput(attrs={'type': 'date'}),
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        exclude = ('resume',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Won 1st place at the National Hackathon 2024'}),
        }
        labels = {
            'description': 'Achievement Description',
        }