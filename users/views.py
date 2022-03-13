import profile
from django.shortcuts import redirect, render
from users.models import Profile
# Create your views here.
def login_view(request):
    return render(request, "Registration/login.html")

def signup_view(request):
    if request.method == "POST":
        profile = Profile()
        profile.username = request.POST.get('username')
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.email = request.POST.get('email')
        profile.password = request.POST.get('password')
        profile.stu_id = request.POST.get('stu_id')
        profile.stu_col = request.POST.get('stu_col')
        profile.mob_num = request.POST.get('mob_num')
        profile.save()
        
        return redirect('home')
    return render(request, "Registration/signup.html")