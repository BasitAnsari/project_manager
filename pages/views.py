from django.shortcuts import redirect, render

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        query = request.POST.get('query')
        request.session['query'] = query
        return redirect('project-list')
    return render(request, "index.html")