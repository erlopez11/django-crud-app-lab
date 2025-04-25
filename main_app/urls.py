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
    path('yarn/create', views.YarnCreate.as_view(), name='yarn-create'),
    path('yarn/<int:pk>/', views.YarnDetail.as_view(), name='yarn-detail'),
    path('yarn/', views.YarnList.as_view(), name='yarn-index'),
    path('yarn/<int:pk>/update/', views.YarnUpdate.as_view(), name='yarn-update'),
    path('yarn/<int:pk>/delete/', views.YarnDelete.as_view(), name='yarn-delete'),
    path('projects/<int:project_id>/associate-yarn/<int:yarn_id>/', views.associate_yarn, name='associate-yarn'),
    path('projects/<int:project_id>/remove-yarn/<int:yarn_id>/', views.remove_yarn, name='remove-yarn'),
]
