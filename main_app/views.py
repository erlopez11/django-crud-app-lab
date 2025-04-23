from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Project
from .forms import ProjectForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {
        'projects': projects
    })

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    project_form = ProjectForm()
    return render(request, 'projects/detail.html', {
        'project': project,
        'project_form': project_form
    })

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
