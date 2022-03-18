from django.urls import path
from .views import project_create_view, project_detail, project_search

urlpatterns = [
    path('project-create/', project_create_view, name= 'project-create'),
    path('project-detail/<int:pk>/', project_detail, name= 'project-detail'),
    path('project-search/', project_search, name= 'project-list'),
]