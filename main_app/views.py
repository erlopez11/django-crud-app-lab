from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Project, Yarn, Note
from .forms import ProjectForm, NoteForm

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects-index')
        else:
            error_message = 'Invalid sign up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/index.html', {
        'projects': projects
    })

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    yarn_available = Yarn.objects.exclude(id__in = project.yarn.all().values_list('id'))
    note_form = NoteForm()
    return render(request, 'projects/detail.html', {
        'project': project,
        'note_form': note_form,
        'yarn': yarn_available
    })

@login_required
def add_note(request, project_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.project_id = project_id
        new_note.save()
    return redirect('project-detail', project_id)

@login_required
def remove_note(request, project_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('project-detail', project_id=project_id)

@login_required
def associate_yarn(request, project_id, yarn_id):
    Project.objects.get(id=project_id).yarn.add(yarn_id)
    return redirect('project-detail', project_id=project_id)

@login_required
def remove_yarn(request, project_id, yarn_id):
    Project.objects.get(id=project_id).yarn.remove(yarn_id)
    return redirect('project-detail', project_id)

class ProjectCreate(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    model = Project

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/projects/'

class YarnCreate(LoginRequiredMixin, CreateView):
    model = Yarn
    fields = ['yarn_name', 'yarn_weight', 'fiber_type', 'color', 'yarn_quantity']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class YarnList(LoginRequiredMixin, ListView):
    model = Yarn

    def get_queryset(self):
        return Yarn.objects.filter(user=self.request.user)

class YarnDetail(LoginRequiredMixin, DetailView):
    model = Yarn

class YarnUpdate(LoginRequiredMixin, UpdateView):
    model = Yarn
    fields = ['yarn_name', 'yarn_weight', 'fiber_type', 'color', 'yarn_quantity']

class YarnDelete(LoginRequiredMixin, DeleteView):
    model = Yarn
    success_url = '/yarn/'