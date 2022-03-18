from multiprocessing import context
from users.models import User, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm,ProfileForm
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()
    return render(request, "Registration/signup.html", {'u_form': u_form, 'p_form': p_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                "error" : "Invalid Username or Password"
            }
            return render(request, "Registration/login.html",context)
    return render(request, "Registration/login.html")
@login_required(login_url='login/')
def profile_view(request):
    profileobj = Profile.objects.get(user= request.user)
    userobj = User.objects.get(id= profileobj.user_id)
    context = {
        'user' : userobj,
        'profile': profileobj,
    }
    return render(request, 'Registration/profile.html', context)

@login_required(login_url='login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'Registration/logout.html')