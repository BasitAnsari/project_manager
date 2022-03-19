from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vectorize(text): return TfidfVectorizer().fit_transform(text).toarray()


def similarity(text1, text2): return cosine_similarity([text1, text2])


def check_plagarism(name, texts):
    vectors = vectorize(texts)
    result = set()
    sim_score = similarity(vectors[0], vectors[1])[0][1]
    name_pair = (name[0], name[1])
    score = name_pair[0], name_pair[1], sim_score
    result.add(score)
    return result

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
        'form': form
    }
    return render(request, "Project/project_form.html", context)


@login_required
def project_detail(request, pk):
    obj = Project.objects.get(id=pk)
    if request.method == 'POST':
        value = request.POST.get('value')
        if value == 'Disapprove':
            obj.is_approved = False
        else:
            obj.is_approved = True
    if obj.plagarised is None:
        domain = obj.domain
        obj2 = Project.objects.filter(domain=domain)

        results = []
        for i in obj2:
            if not i.id == obj.id:
                name = [obj.title, i.title]
                texts = [obj.statement, i.statement]
                p = list(check_plagarism(name, texts))[0]
                pn = float(p[2])*100
                pn = round(pn, 2)
                print(pn)
                results.append((p[1], pn))
        print(results)
        big = 0
        for title, num in results:
            if num > big:
                big = num
        plag = max(results, default=0)
        obj.plagarised = plag
        # obj.plagarised_with = ptitle
    obj.save()
    context = {
        'object': obj
    }
    return render(request, "Project/project_details.html", context)


def project_search(request):
    query = request.session['query']
    if query is not None:
        qs = Project.objects.filter(title__icontains=query, is_approved=True)
    else:
        qs = Project.objects.filter(is_approved=True)
    if request.method == 'POST':
        title = request.POST.get('title')
        domain = request.POST.get('domain')
        category = request.POST.get('category')
        if title is not None:
            qs = qs.filter(title__icontains=title)
        if domain is not None:
            qs = qs.filter(domain__icontains=domain)
        if category is not None:
            qs = qs.filter(category__icontains=category)
    context = {
        'qs': qs
    }
    return render(request, 'Project/project_list.html', context)
