from django.urls import path
from .views import StaffCreateView, StaffDeleteView, StaffUpdateView, StaffListView,staffSearchView

urlpatterns = [
    path('create/',StaffCreateView.as_view(),name='create_staff'),
    path('retrive/',StaffListView.as_view(),name='retrive_staff'),
    path('update/<int:pk>/',StaffUpdateView.as_view(),name='update_staff'),
    path('delete/<int:pk>/',StaffDeleteView.as_view(),name='delete_staff'),
    path('search/',staffSearchView,name='search_staff'),
]