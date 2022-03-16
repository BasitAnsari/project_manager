from turtle import title
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'statement',
            'domain',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(),
            'Domain': forms.TextInput(),
            'Category': forms.TextInput(),
            'Statement': forms.TextInput(),
        }