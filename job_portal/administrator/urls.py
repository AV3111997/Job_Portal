from django.urls import path
from .views import EmployerListView,EmployerDeleteView,CandidateListView,CandidateDeleteView

urlpatterns = [
    # path('job_category/', views.job_category_list, name='job_category_list'),
    # path('job_category/create/', views.job_category_create, name='job_category_create'),
    # path('job_category/update/<int:id>/', views.job_category_update, name='job_category_update'),
    # path('job_category/delete/<int:id>/', views.job_category_delete, name='job_category_delete'),
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('employer/<int:pk>/delete/', EmployerDeleteView.as_view(), name='employer_delete'),
    path('listcandidates/', CandidateListView.as_view(), name='listcandidates'),
    path('candidate_delete/<int:pk>/', CandidateDeleteView.as_view(), name='candidate_delete'),
]




        
