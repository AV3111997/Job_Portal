from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("articles", views.ArticlesView.as_view(), name="articles"),
    path("faq", views.FAQView.as_view(), name="faq"),
    path("pricing", views.PricingView.as_view(), name="pricing"),
    path("employers_list", views.employers_list, name="employers_list"),
    path("job_list", views.job_list, name="job_list"),
    path("job_details/<int:pk>", views.JobDetailView.as_view(), name="job_details"),
    path("employers_details/<int:pk>", views.EmployerDetailView.as_view(), name="employers_details"),
    path("candidate", views.CandidateView.as_view(), name="candidate"),
    path("userdashboard", views.UserDashboardView.as_view(), name="userdashboard"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("managejobs/", views.ManageJobsView.as_view(), name="managejobs"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("terms/", views.TermView.as_view(), name="terms"),
    # path("applied_jobs", views.AppliedJobsView.as_view(), name="applied_jobs"),
    path("applicants_jobs", views.ApplicantsJobsView.as_view(), name="applicants_jobs"),
    path("manage_jobs/", views.ManageJobsView.as_view(), name="manage_jobs"),
    path(
        "candidate_profile/",
        views.CandidateProfileView.as_view(),
        name="candidate_profile",
    ),
    path(
        "employer_profile/",
        views.EmployerProfileView.as_view(),
        name="employer_profile",
    ),
    path("jobform/", views.JobPostingCreateView.as_view(), name="jobform"),
    path(
        "jobpost/update/<int:pk>/",
        views.JobPostingUpdateView.as_view(),
        name="jobpost_update",
    ),
    path("candidates/", views.candidate_list, name="candidate_list"),
    path(
        "category/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"
    ),
    path(
        "save_job/<int:job_id>/<int:candidate_id>/",
        views.SaveJobView.as_view(),
        name="save_job",
    ),
    path("saved_jobs/", views.SavedJobsView.as_view(), name="candidate_saved_jobs"),
    path(
        "delete_saved_job/<int:pk>/",
        views.DeleteSavedJobView.as_view(),
        name="delete_saved_job",
    ),
    path("result/", views.search, name="search"),
    path("upload_cv/", views.CVUploadView.as_view(), name="cv_upload"),


    path('apply/<int:job_id>/',views.ApplyForJobView.as_view(), name='apply_for_job'),
    path('applied-jobs/', views.AppliedJobsListView.as_view(), name='applied_jobs'),
    path(
        "delete_applied_job/<int:pk>/",
        views.DeleteAppliedJobView.as_view(),
        name="delete_applied_job",
    ),
]


        
