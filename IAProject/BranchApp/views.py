from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Branch
from django.urls import reverse_lazy
from .forms import BranchModelForm

# Create your views here.
class BranchCreateView(CreateView):
    model = Branch
    form_class = BranchModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_branch')

class BranchListView(ListView):
    model = Branch

class BranchUpdateView(UpdateView):
    model = Branch
    form_class = BranchModelForm
    # fields = '__all__'
    success_url = reverse_lazy('retrive_branch')

class BranchDeleteView(DeleteView):
    model = Branch
    success_url = reverse_lazy('retrive_branch')


def branchSearchView(request):
    n = request.GET.get('branch_name')
    print(f"Searching {n}")
    # branchs = Branch.objects.filter(name__contains=n)
    branch = Branch.objects.filter(name__contains=n).first()
    print("branch:-",branch)
    print("dir(branch):-",dir(branch))
    profs = branch.prof_set.all()
    studs = branch.student_set.all()
    print(f"studs-{studs}")
    template_name = "BranchApp/branch_search_list.html"
    context = {'branch':branch,'branch_name':n,'profs_list':profs,'studs_list':studs}
    return render(request,template_name,context)
