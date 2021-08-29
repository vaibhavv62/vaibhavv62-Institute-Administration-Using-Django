from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Dept
from django.urls import reverse_lazy

# Create your views here.
class DeptCreateView(CreateView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('retrive_dept')

class DeptListView(ListView):
    model = Dept

class DeptUpdateView(UpdateView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('retrive_dept')

class DeptDeleteView(DeleteView):
    model = Dept
    success_url = reverse_lazy('retrive_dept')

'''
def deptSearchView(request):
    n = request.GET.get('dept_name')
    print(f"Searching {n}")
    # depts = Dept.objects.filter(name__contains=n)
    dept = Dept.objects.filter(name__contains=n).first()
    profs = dept.prof_set.all()
    studs = dept.student_set.all()
    print(f"studs-{studs}")
    template_name = "CollegeApp/dept_search_list.html"
    context = {'dept':dept,'dept_name':n,'profs_list':profs,'studs_list':studs}
    return render(request,template_name,context)
'''