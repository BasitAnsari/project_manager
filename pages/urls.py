from unicodedata import name
from django import views
from django.urls import path
from .views import home_view
urlpatterns = [
    path('', home_view, name='home')
]