from django.urls import path
from .views import StudentCreateView, StudentDeleteView, StudentUpdateView, StudentListView, studentSearchView

urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='create_stud'),
    path('retrive/',StudentListView.as_view(),name='retrive_stud'),
    path('update/<int:pk>/',StudentUpdateView.as_view(),name='update_stud'),
    path('delete/<int:pk>/',StudentDeleteView.as_view(),name='delete_stud'),
    path('search/',studentSearchView,name='search_stud'),
]