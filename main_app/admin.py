from django.contrib import admin
from .models import Project, Note, Yarn

admin.site.register([Project, Note, Yarn])
