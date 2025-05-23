from django import forms
from .models import Project, Note

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'pattern', 'progress_status', 'needle_size', 'cast_on', 'cast_off']
        widgets = {
            'cast_on': forms.DateInput(
                format=('%y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'cast_off': forms.DateInput(
                format=('%y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'notes', 'current_row']
        widgets = {
            'date': forms.DateInput(
                format=('%y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }