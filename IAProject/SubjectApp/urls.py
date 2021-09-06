from django.urls import path
from .views import SubjectCreateView, SubjectDeleteView, SubjectUpdateView, SubjectListView, subjectSearchView,subjectDeleteAllView,populateFakeRecordsView

urlpatterns = [
    path('create/',SubjectCreateView.as_view(),name='create_subj'),
    path('retrive/',SubjectListView.as_view(),name='retrive_subj'),
    path('update/<int:pk>/',SubjectUpdateView.as_view(),name='update_subj'),
    path('delete/<int:pk>/',SubjectDeleteView.as_view(),name='delete_subj'),
    path('delete-all/',subjectDeleteAllView,name='delete_all_subj'),
    path('search/',subjectSearchView,name='search_subj'),
    path('populate/',populateFakeRecordsView,name='populate_subj'),
]