from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project

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
    return render(request, 'projects/detail.html', {
        'project': project,
    })

class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'pattern', 'progress_status', 'needle_size', 'cast_on', 'cast_off']

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'pattern', 'progress_status', 'needle_size', 'cast_on', 'cast_off']

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'