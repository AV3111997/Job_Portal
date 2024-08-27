from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Candidate, SocialNetwork, Contact, JobPosting
from .forms import CandidateForm, SocialNetworkForm, ContactForm, JobPostingForm
from django.urls import reverse_lazy

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
    
class EmployeeJobsView(TemplateView):
    template_name = 'employee.html'

class CandidateProfile(TemplateView):
    def get(self, request):
        candidate_form = CandidateForm()
        socialnetwork_form = SocialNetworkForm()
        contact_form = ContactForm()
        return render(request, 'candidate_profile.html', {
            'candidate_form': candidate_form,
            'socialnetwork_form': socialnetwork_form,
            'contact_form': contact_form,
        })

    def post(self, request):
        candidate_form = CandidateForm(request.POST, request.FILES)
        socialnetwork_form = SocialNetworkForm(request.POST)
        contact_form = ContactForm(request.POST)

        if candidate_form.is_valid() and socialnetwork_form.is_valid() and contact_form.is_valid():
            candidate_form.save()
            socialnetwork_form.save()
            contact_form.save()
            return redirect('userdashboard')

        return render(request, 'candidate_profile.html', {
            'candidate_form': candidate_form,
            'socialnetwork_form': socialnetwork_form,
            'contact_form': contact_form,
        })

class JobPostingCreateView(FormView):
    form_class = JobPostingForm
    template_name = 'jobposting_form.html'  # Make sure this template exists
    success_url = reverse_lazy('jobform')  # Redirect after successful form submission

    def form_valid(self, form):
        # Here you can perform additional actions if needed before saving
        form.save()  # Save the form data
        return super().form_valid(form)
