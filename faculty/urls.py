from django.urls import path
from .views import faculty_view

urlpatterns = [
    path('faculty/', faculty_view, name= 'faculty'),
]