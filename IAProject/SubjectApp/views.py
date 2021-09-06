from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Subject
from django.urls import reverse_lazy
from .forms import SubjectModelForm
from django.conf import settings

# Create your views here.
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_subj')

class SubjectListView(ListView):
    model = Subject

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_subj')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('retrive_subj')

def subjectDeleteAllView(request):
    if request.method == 'POST':
        Subject.objects.all().delete()
        return redirect('retrive_subj')
    template_name = "SubjectApp/subject_confirm_delete_all.html"
    context = {}
    return render(request,template_name,context)

def subjectSearchView(request):
    n = request.GET.get('subj_name')
    print(f"Searching {n}")
    subjects = Subject.objects.filter(name__contains=n)
    template_name = "SubjectApp/subject_search_list.html"
    context = {'object_list':subjects,'subj_name':n}
    return render(request,template_name,context)

def populateFakeRecordsView(request):
    import sys
    # print(settings.BASE_DIR)
    sys.path.append(settings.BASE_DIR)
    import populate_subjects
    populate_subjects.addFakeSubjects(20)
    return redirect('retrive_subj')
