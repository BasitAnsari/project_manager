from django.urls import path
from .views import signup_view,login_view, profile_view,logout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name= 'logout'),
    path('signup/', signup_view, name = 'sign-up'),
    path('profile/', profile_view, name = 'profile'),
]