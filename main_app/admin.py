from django.contrib import admin
from .models import Project, Note

admin.site.register([Project, Note])
