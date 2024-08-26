from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import JobPosting
from .forms import JobPostingForm

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ArticlesView(TemplateView):
    template_name = 'article_page.html'


class FAQView(TemplateView):
    template_name = 'faq.html'


class PricingView(TemplateView):
    template_name = 'pricing.html'


class JobDetailsView(TemplateView):
    template_name = 'job_details.html'


class CandidateView(TemplateView):
    template_name = 'candidate.html'


class EmployersListView(TemplateView):
    template_name = 'employerslist.html'


class JobListView(TemplateView):
    template_name = 'findjoblist.html'


class UserDashboardView(TemplateView):
    template_name = 'userdashboard.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'



class TermView(TemplateView):
    template_name = 'terms.html'    

class AppliedJobsView(TemplateView):
    template_name = 'applied_jobs.html'

class ApplicantsJobsView(TemplateView):
    template_name = 'applicants_jobs.html'
    
class ManageJobsView(TemplateView):
    template_name = 'manage_jobs.html'

# class EmployeeJobsView(TemplateView):
#     template_name = 'employee.html'



class JobPostingCreateView(FormView):
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'employee.html'  # Ensure this template exists and is set up correctly
    success_url = reverse_lazy('jobform')  # Redirect after successful form submission

    def form_valid(self, form):
        # Here you can perform additional actions if needed before saving
        return super().form_valid(form)
