from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm
# Create your views here.
@login_required
def project_create_view(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.institute = request.user.profile.stu_col
            instance.save()
            return redirect('home')
    context = {
        'form' : form
        }
    return render(request, "Project/project_form.html",context)
@login_required
def project_detail(request,pk):
    obj = Project.objects.get(id= pk)
    if request.method == 'POST':
        obj.is_approved = True
    context = {
        'object': obj
    }
    return render(request,"Project/project_details.html", context)
        
def project_search(request):
    query = request.session['query']
    if query is not None:
        qs = Project.objects.filter(title__icontains= query)
    else :
        qs = Project.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        domain = request.POST.get('domain')
        category = request.POST.get('category')
        if title is not None :
            qs = qs.filter(title__icontains= title)
        if domain is not None :
            qs = qs.filter(domain__icontains= domain)
        if category is not None :
            qs = qs.filter(category__icontains= category)
    context = {
        'qs' : qs
    }
    return render(request, 'Project/project_list.html',context)