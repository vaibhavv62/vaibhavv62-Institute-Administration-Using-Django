from django.urls import path
from .views import StudentCreateView, StudentDeleteView, StudentUpdateView, StudentListView, studentLoginView, studentSearchView, StudentDashboardView, studentSubjectsView, studentLogoutView

urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='create_stud'),
    path('retrive/',StudentListView.as_view(),name='retrive_stud'),
    path('update/<int:pk>/',StudentUpdateView.as_view(),name='update_stud'),
    path('delete/<int:pk>/',StudentDeleteView.as_view(),name='delete_stud'),
    path('search/',studentSearchView,name='search_stud'),
    path('dashboard/',StudentDashboardView.as_view(),name='dashboard_stud'),
    path('my-subjects/',studentSubjectsView,name='my_subs_stud'),
    path('login/',studentLoginView,name='login_stud'),
    path('logout/',studentLogoutView,name='logout_stud'),
]