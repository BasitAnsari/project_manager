from django.shortcuts import redirect, render
from project.models import Project
# Create your views here.
def faculty_view(request):
    if request.user.profile.is_faculty:
        faculty_col = request.user.profile.stu_col
        project_qs = Project.objects.filter(institute = faculty_col)
        context = {
            "qs" : project_qs
        }
        return render(request, "Faculty/faculty_profile.html", context)
    else:
        return redirect('home')
        