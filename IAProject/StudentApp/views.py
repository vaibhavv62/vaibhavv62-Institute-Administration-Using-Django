from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Student
from django.urls import reverse_lazy
from .forms import StudentModelForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings


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

def studentDeleteAllView(request):
    if request.method == 'POST':
        Student.objects.all().delete()
        return redirect('retrive_stud')
    template_name = "StudentApp/student_confirm_delete_all.html"
    context = {}
    return render(request,template_name,context)

def studentSearchView(request):
    n = request.GET.get('stud_name')
    print(f"Searching {n}")
    students = Student.objects.filter(name__contains=n)
    template_name = "StudentApp/student_search_list.html"
    context = {'object_list':students,'stud_name':n}
    return render(request,template_name,context)

class StudentDashboardView(TemplateView):
    template_name = 'StudentApp/student_dashboard.html'


def studentSubjectsView(request):
    # n = request.GET.get('stud_name')
    # print(f"Searching {n}")
    # students = Student.objects.filter(name__contains=n)
    template_name = "StudentApp/student_subject_list.html"
    context = {}
    return render(request,template_name,context)

def studentLoginView(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pw')

        if not un or not pw:
            messages.error(request,'Both Username & Password are required!')
            return redirect('login_stud')
        
        user_obj = User.objects.filter(username = un).first()
        print('user.first():',user_obj)

        if user_obj is None:
            messages.error(request,f'User Not Found with username-{un}!')
            return redirect('login_stud')

        user = authenticate(username = un, password = pw)
        if user is not None:
            login(request,user)
        else:
            messages.error(request,'Invalid Credentials')
    
    template_name = "StudentApp/student_login.html"
    context = {}
    return render(request,template_name,context)


def studentLogoutView(request):
    logout(request)
    return redirect('login_stud')

def populateFakeRecordsView(request):
    import sys
    # print(settings.BASE_DIR)
    sys.path.append(settings.BASE_DIR)
    import populate_students
    try:
        populate_students.addFakeStudents(20)
    except:
        populateFakeRecordsView(request)
    return redirect('retrive_stud')