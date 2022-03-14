from django.urls import path
from .views import signup_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='Registration/login.html'), name= 'login'),
    path('signup', signup_view, name = 'sign-up'),
]