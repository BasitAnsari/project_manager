from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
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
            instance.save()
            return redirect('home')
    context = {
        'form' : form
        }
    return render(request, "Project/project_form.html",context)
        