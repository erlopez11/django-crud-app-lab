from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name='projects-index'),
    path('projects/<int:project_id>', views.project_detail, name='project-detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('projects/<int:project_id>/add-note/', views.add_note, name='add-note'),
]
