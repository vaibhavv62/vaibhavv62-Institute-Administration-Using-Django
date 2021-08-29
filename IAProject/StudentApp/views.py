from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Student
from django.urls import reverse_lazy
from .forms import StudentModelForm

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_stud')

class StudentListView(ListView):
    model = Student

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_stud')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('retrive_stud')

def studentSearchView(request):
    n = request.GET.get('stud_name')
    print(f"Searching {n}")
    students = Student.objects.filter(name__contains=n)
    template_name = "StudentApp/student_search_list.html"
    context = {'object_list':students,'stud_name':n}
    return render(request,template_name,context)


