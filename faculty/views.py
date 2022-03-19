from django.shortcuts import redirect, render
from project.models import Project
# Create your views here.
def faculty_view(request):
    if request.user.profile.is_faculty:
        faculty_col = request.user.profile.stu_col
        qs = Project.objects.filter(institute = faculty_col)
        if request.method == 'POST':
            title = request.POST.get('title')
            domain = request.POST.get('domain')
            category = request.POST.get('category')
            apr = request.POST.get('apr')
            print(apr)
            if title is not None :
                qs = qs.filter(title__icontains= title)
            if domain is not None :
                qs = qs.filter(domain__icontains= domain)
            if category is not None :
                qs = qs.filter(category__icontains= category)
            if apr is not None :
                if apr == 'apr':
                    qs = qs.filter(is_approved= True)
                else:
                    qs = qs.filter(is_approved= False)
        context = {
            "qs" : qs
        }
        return render(request, "Faculty/faculty_profile.html", context)
    else:
        return redirect('home')
        