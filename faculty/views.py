from django.shortcuts import redirect, render
from project.models import Project
# Create your views here.
def faculty_view(request):
    if request.user.profile.is_faculty:
        faculty_col = request.user.profile.stu_col
        print(faculty_col)
        # project_qs = Project.objects.filter(user.profile.stu_col = faculty_col)
        return render(request, "Faculty/faculty_profile.html")
    else:
        return redirect('home')
        