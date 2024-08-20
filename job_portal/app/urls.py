from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('articles', views.ArticlesView.as_view(), name='articles'),
    path('faq', views.FAQView.as_view(), name='faq'),
    path('pricing', views.PricingView.as_view(), name='pricing'),
    path('employers_list', views.EmployersListView.as_view(), name='employers_list'),
    path('job_list', views.JobListView.as_view(), name='job_list'),
    path('job_details', views.JobDetailsView.as_view(), name='job_details'),
    path('candidate', views.CandidateView.as_view(), name='candidate'),
    path('userdashboard', views.UserDashboardView.as_view(), name='userdashboard'),
    path('applied_jobs', views.AppliedJobsView.as_view(), name='applied_jobs'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('applicants_jobs', views.ApplicantsJobsView.as_view(), name='applicants_jobs'),
]
