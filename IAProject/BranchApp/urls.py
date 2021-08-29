from django.urls import path
from .views import BranchCreateView, BranchDeleteView, BranchUpdateView, BranchListView, branchSearchView

urlpatterns = [
    path('create/',BranchCreateView.as_view(),name='create_branch'),
    path('retrive/',BranchListView.as_view(),name='retrive_branch'),
    path('update/<int:pk>/',BranchUpdateView.as_view(),name='update_branch'),
    path('delete/<int:pk>/',BranchDeleteView.as_view(),name='delete_branch'),
    path('search/',branchSearchView,name='search_branch'),
]