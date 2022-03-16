from django.urls import path
from .views import project_create_view

urlpatterns = [
    path('project-create/', project_create_view, name= 'project-create'),
]