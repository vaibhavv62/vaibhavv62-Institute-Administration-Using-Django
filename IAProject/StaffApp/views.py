from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Staff
from django.urls import reverse_lazy
from .forms import StaffModelForm

# Create your views here.
class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_staff')

class StaffListView(ListView):
    model = Staff


class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_staff')

class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy('retrive_staff')

def staffSearchView(request):
    n = request.GET.get('staff_name')
    print(f"Searching {n}")
    staffs = Staff.objects.filter(name__contains=n)
    print("staffs:-",staffs)
    template_name = "StaffApp/staff_search_list.html"
    context = {'object_list':staffs,'staff_name':n}
    return render(request,template_name,context)


