# resume/models.py
from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template_choice = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Resume ({self.template_choice})"

class PersonalDetails(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)

class ProfessionalSummary(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    summary = models.TextField(blank=True)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_work_here = models.BooleanField(default=False)
    responsibilities = models.TextField()
    is_internship = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.institution

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    skills_list = models.TextField()

    def __str__(self):
        return f"{self.category}"

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_link = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.project_name

class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    date_issued = models.DateField()
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description[:50]