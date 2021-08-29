from django.urls import path
from .views import DeptCreateView, DeptDeleteView, DeptUpdateView, DeptListView#, deptSearchView

urlpatterns = [
    path('create/',DeptCreateView.as_view(),name='create_dept'),
    path('retrive/',DeptListView.as_view(),name='retrive_dept'),
    path('update/<int:pk>/',DeptUpdateView.as_view(),name='update_dept'),
    path('delete/<int:pk>/',DeptDeleteView.as_view(),name='delete_dept'),
    # path('search/',deptSearchView,name='search_dept'),
]