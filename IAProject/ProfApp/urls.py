from django.urls import path
from .views import ProfCreateView, ProfDeleteView, ProfUpdateView, ProfListView,professorSearchView,professorDeleteAllView,populateFakeRecordsView

urlpatterns = [
    path('create/',ProfCreateView.as_view(),name='create_prof'),
    path('retrive/',ProfListView.as_view(),name='retrive_prof'),
    path('update/<int:pk>/',ProfUpdateView.as_view(),name='update_prof'),
    path('delete/<int:pk>/',ProfDeleteView.as_view(),name='delete_prof'),
    path('delete-all/',professorDeleteAllView,name='delete_all_prof'),
    path('search/',professorSearchView,name='search_prof'),
    path('populate/',populateFakeRecordsView,name='populate_prof'),
]