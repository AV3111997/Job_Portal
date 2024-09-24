from django.urls import path
from .views import EmployerListView,EmployerDeleteView
from .views import (
    EmployerListView,EmployerDeleteView ,
    CandidateListView,CandidateDeleteView,
    LanguageListView,
    LanguageCreateView,
    LanguageUpdateView,
    LanguageDeleteView,
    LocationListView,
    LocationCreateView,
    LocationUpdateView,
    LocationDeleteView,
    JobCategoryListView,
    JobCategoryCreateView,
    JobCategoryUpdateView,
    JobCategoryDeleteView,
    ProfessionalSkillCreateView,
    ProfessionalSkillUpdateView,
    ProfessionalSkillDeleteView,
    ProfessionalSkillListView,
    )

urlpatterns = [
    # path('job_category/', views.job_category_list, name='job_category_list'),
    # path('job_category/create/', views.job_category_create, name='job_category_create'),
    # path('job_category/update/<int:id>/', views.job_category_update, name='job_category_update'),
    # path('job_category/delete/<int:id>/', views.job_category_delete, name='job_category_delete'),
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('employer/<int:pk>/delete/', EmployerDeleteView.as_view(), name='employer_delete'),
    path('listcandidates/', CandidateListView.as_view(), name='listcandidates'),
    path('candidate_delete/<int:pk>/', CandidateDeleteView.as_view(), name='candidate_delete'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('languages/add/', LanguageCreateView.as_view(), name='language_add'),
    path('languages/update/<int:pk>/', LanguageUpdateView.as_view(), name='language_update'),
    path('languages/delete/<int:pk>/', LanguageDeleteView.as_view(), name='language_delete'),
    path('location/', LocationListView.as_view(), name='location_list'),
    path('location/add/', LocationCreateView.as_view(), name='location_add'),
    path('location/update/<int:pk>/', LocationUpdateView.as_view(), name='location_update'),
    path('location/delete/<int:pk>/', LocationDeleteView.as_view(), name='location_delete'),
    path('job_category/', JobCategoryListView.as_view(), name='jobcategory_list'),
    path('job_category/add/', JobCategoryCreateView.as_view(), name='jobcategory_add'),
    path('job_category/update/<int:pk>/', JobCategoryUpdateView.as_view(), name='jobcategory_update'),
    path('job_category/delete/<int:pk>/', JobCategoryDeleteView.as_view(), name='jobcategory_delete'),
    path('professional_skill/', ProfessionalSkillListView.as_view(), name='professionalskill_list'),
    path('professional_skill/add/', ProfessionalSkillCreateView.as_view(), name='professionalskill_add'),
    path('professional_skill/update/<int:pk>/', ProfessionalSkillUpdateView.as_view(), name='professionalskill_update'),
    path('professional_skill/delete/<int:pk>/', ProfessionalSkillDeleteView.as_view(), name='professionalskill_delete'),

]


        
