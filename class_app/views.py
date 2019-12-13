from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import (
    CreateView,DetailView,ListView,UpdateView,DeleteView
)
from django.views import View
from .models import ClassApp
from django.urls import reverse
from .form import ClassAppForm

class ClassCreateView(CreateView):
    template_name = 'class_create_view.html'
    form_class = ClassAppForm
    queryset = ClassApp.objects.all()
    success_url = ''

    # def get_success_url(self):
    #     return 'class/'



class ClassListView(ListView):
    template_name = "class_app.html"
    queryset = ClassApp.objects.all()

class ClassDetailView(DetailView):
    template_name = "class_Detail.html"
    queryset = ClassApp.objects.all()

    # filter(id__gt=1) meaning id is greater than 1, used in a queryset


    # helps to use id instead of pk
    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return get_object_or_404(ClassApp, id=id)

class ClassUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = ClassAppForm
    queryset = ClassApp.objects.all()

class ClassDeleteView(DeleteView):
    template_name = 'delete.html'
    form_class = ClassAppForm
    queryset = ClassApp.objects.all()
    # success_url = '/class/'


    def get_success_url(self):
        return reverse('class_app:class_list_view')

class CourseView(View):
    def my_fab(self):

