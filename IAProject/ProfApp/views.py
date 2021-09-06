from django.shortcuts import render,redirect
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Prof
from django.urls import reverse_lazy
from .forms import ProfModelForm
from django.conf import settings

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

def professorDeleteAllView(request):
    if request.method == 'POST':
        Prof.objects.all().delete()
        return redirect('retrive_prof')
    template_name = "ProfApp/prof_confirm_delete_all.html"
    context = {}
    return render(request,template_name,context)

def professorSearchView(request):
    n = request.GET.get('prof_name')
    print(f"Searching {n}")
    profs = Prof.objects.filter(name__contains=n)
    print("profs:-",profs)
    template_name = "ProfApp/prof_search_list.html"
    context = {'object_list':profs,'prof_name':n}
    return render(request,template_name,context)
    
def populateFakeRecordsView(request):
    import sys
    # print(settings.BASE_DIR)
    sys.path.append(settings.BASE_DIR)
    import populate_professors
    try:
        populate_professors.addFakeProfessors(20)
    except:
        populateFakeRecordsView()
    return redirect('retrive_prof')


