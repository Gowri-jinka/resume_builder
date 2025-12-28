# resume/views.py - FINAL STABLE VERSION
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import (
    Resume, PersonalDetails, ProfessionalSummary, Experience, Education, 
    Skill, Project, Certification, Achievement
)
from .forms import (
    PersonalDetailsForm, ProfessionalSummaryForm, ExperienceForm, EducationForm, 
    SkillForm, ProjectForm, CertificationForm, AchievementForm
)

# --- CORE VIEWS ---
def welcome_view(request):
    return render(request, 'resume/welcome.html')

def auth_view(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid(): user = form.save(); login(request, user); return redirect('home')
        elif 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid(): user = form.get_user(); login(request, user); return redirect('home')
    return render(request, 'resume/auth.html', {'form': UserCreationForm(), 'login_form': AuthenticationForm()})

@login_required
def home_view(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resume/home.html', {'resumes': resumes})

def logout_view(request):
    logout(request)
    return redirect('welcome')

# --- RESUME CREATION & BUILDER ---
@login_required
def choose_template_view(request):
    if request.method == 'POST':
        template_choice = request.POST.get('template')
        new_resume = Resume.objects.create(user=request.user, template_choice=template_choice)
        return redirect('build_single_column', resume_id=new_resume.id)
            
    return render(request, 'resume/choose_template.html')

@login_required
def edit_resume_dispatcher_view(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    return redirect('build_single_column', resume_id=resume.id)

@login_required
def build_single_column_view(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'personal_details':
            instance, _ = PersonalDetails.objects.get_or_create(resume=resume)
            form = PersonalDetailsForm(request.POST, instance=instance)
            if form.is_valid(): form.save()
        elif action == 'summary':
            instance, _ = ProfessionalSummary.objects.get_or_create(resume=resume)
            form = ProfessionalSummaryForm(request.POST, instance=instance)
            if form.is_valid(): form.save()
        elif action == 'add_education':
            form = EducationForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
        elif action == 'add_experience':
            form = ExperienceForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
        elif action == 'add_skill':
            form = SkillForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
        elif action == 'add_project':
            form = ProjectForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
        elif action == 'add_certification':
            form = CertificationForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
        elif action == 'add_achievement':
            form = AchievementForm(request.POST)
            if form.is_valid(): entry = form.save(commit=False); entry.resume = resume; entry.save()
            
        return redirect('build_single_column', resume_id=resume.id)

    context = {
        'resume': resume,
        'personal_details_form': PersonalDetailsForm(instance=getattr(resume, 'personaldetails', None)),
        'summary_form': ProfessionalSummaryForm(instance=getattr(resume, 'professionalsummary', None)),
        'education_form': EducationForm(),
        'experience_form': ExperienceForm(),
        'skill_form': SkillForm(),
        'project_form': ProjectForm(),
        'certification_form': CertificationForm(),
        'achievement_form': AchievementForm(),
    }
    return render(request, 'resume/build_single_column.html', context)

# --- HELPER & DELETE/UPDATE VIEWS ---
def redirect_to_builder(resume):
    return redirect('build_single_column', resume_id=resume.id)

@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    resume.delete()
    return redirect('home')

@login_required
def update_education(request, education_id):
    entry = get_object_or_404(Education, id=education_id, resume__user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_education(request, education_id):
    entry = get_object_or_404(Education, id=education_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)

@login_required
def update_experience(request, experience_id):
    entry = get_object_or_404(Experience, id=experience_id, resume__user=request.user)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_experience(request, experience_id):
    entry = get_object_or_404(Experience, id=experience_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)
    
@login_required
def update_skill(request, skill_id):
    entry = get_object_or_404(Skill, id=skill_id, resume__user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_skill(request, skill_id):
    entry = get_object_or_404(Skill, id=skill_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)

@login_required
def update_project(request, project_id):
    entry = get_object_or_404(Project, id=project_id, resume__user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_project(request, project_id):
    entry = get_object_or_404(Project, id=project_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)

@login_required
def update_certification(request, certification_id):
    entry = get_object_or_404(Certification, id=certification_id, resume__user=request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_certification(request, certification_id):
    entry = get_object_or_404(Certification, id=certification_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)

@login_required
def update_achievement(request, achievement_id):
    entry = get_object_or_404(Achievement, id=achievement_id, resume__user=request.user)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=entry)
        if form.is_valid(): form.save()
    return redirect_to_builder(entry.resume)

@login_required
def delete_achievement(request, achievement_id):
    entry = get_object_or_404(Achievement, id=achievement_id, resume__user=request.user)
    resume = entry.resume; entry.delete()
    return redirect_to_builder(resume)
