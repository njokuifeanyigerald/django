from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectForm, RawProjectForm

# Create your views here.
def home_view(request,*args,**kwargs):
    queryset = Project.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "home.html", context)

def about_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'about.html', context)
def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, "contact.html", context)

def project_detail_view(request):
   my_form = RawProjectForm()
   if request.method == "POST":
       my_form = RawProjectForm(request.POST)
       if my_form.is_valid():
           Project.objects.create(**my_form.cleaned_data)
           my_form = RawProjectForm
   context = {
        'form': my_form
   }
   return render(request, "project/detail.html",context)

# def render_initial_data(request):
#     initial_data = {
#         "title": "my awesome title"
#     }
#     obj = Project.objects.get(id=1)
#     form = ProjectForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         form=ProjectForm
#     context = {
#         'form': form
#     }
#
#
#     return render(request, "project/render.html", context)

def render_initial_data(request, id):
   # form = Project.objects.get(id=id)
   form = get_object_or_404(Project, id=id)


   control = {
       "control": form
   }
   return render(request, "project/render.html", control)

def project_delete(request, id):
    form = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form.delete()
        return redirect("/")
    context = {
        "form":form
    }

    return render(request, "project/project_delete.html", context)

def project_list(request):
    queryset = Project.objects.all()

    context = {
        "object_list":queryset
    }

    return render(request, "project/project_list.html", context)