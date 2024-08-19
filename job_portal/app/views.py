from django.shortcuts import render
from django.views.generic import TemplateView

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

class AppliedJobsView(TemplateView):
    template_name = 'applied_jobs.html'

class ManageJobsView(TemplateView):
    template_name = 'manage_jobs.html'
