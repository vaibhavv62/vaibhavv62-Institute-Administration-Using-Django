from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Prof
from django.urls import reverse_lazy
from .forms import ProfModelForm

# Create your views here.
class ProfCreateView(CreateView):
    model = Prof
    form_class = ProfModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_prof')

class ProfListView(ListView):
    model = Prof


class ProfUpdateView(UpdateView):
    model = Prof
    form_class = ProfModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_prof')

class ProfDeleteView(DeleteView):
    model = Prof
    success_url = reverse_lazy('retrive_prof')

def professorSearchView(request):
    n = request.GET.get('prof_name')
    print(f"Searching {n}")
    profs = Prof.objects.filter(name__contains=n)
    print("profs:-",profs)
    template_name = "ProfApp/prof_search_list.html"
    context = {'object_list':profs,'prof_name':n}
    return render(request,template_name,context)


