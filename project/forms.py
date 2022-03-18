from turtle import title
from django import forms
from .models import Project
from users.models import User
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
            'Category': forms.Select(),
            'Statement': forms.TextInput(),
        }