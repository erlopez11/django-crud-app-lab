from django import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project, Yarn
from .forms import ProjectForm, NoteForm

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
    yarn_available = Yarn.objects.exclude(id__in = project.yarn.all().values_list('id'))
    note_form = NoteForm()
    return render(request, 'projects/detail.html', {
        'project': project,
        'note_form': note_form,
        'yarn': yarn_available
    })

def add_note(request, project_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.project_id = project_id
        new_note.save()
    return redirect('project-detail', project_id)

def associate_yarn(request, project_id, yarn_id):
    Project.objects.get(id=project_id).yarn.add(yarn_id)
    return redirect('project-detail', project_id=project_id)

def remove_yarn(request, project_id, yarn_id):
    Project.objects.get(id=project_id).yarn.remove(yarn_id)
    return redirect('project-detail', project_id= project_id)

class ProjectCreate(CreateView):
    form_class = ProjectForm
    model = Project
    #fields = ['name', 'pattern', 'progress_status', 'needle_size', 'cast_on', 'cast_off']

class ProjectUpdate(UpdateView):
    form_class = ProjectForm
    model = Project
    #fields = ['name', 'pattern', 'progress_status', 'needle_size', 'cast_on', 'cast_off']

class ProjectDelete(DeleteView):
    model = Project
    success_url = '/projects/'

class YarnCreate(CreateView):
    model = Yarn
    fields = ['yarn_name', 'yarn_weight', 'fiber_type', 'color', 'yarn_quantity']

class YarnList(ListView):
    model = Yarn

class YarnDetail(DetailView):
    model = Yarn

class YarnUpdate(UpdateView):
    model = Yarn
    fields = ['yarn_name', 'yarn_weight', 'fiber_type', 'color', 'yarn_quantity']

class YarnDelete(DeleteView):
    model = Yarn
    success_url = '/yarn/'