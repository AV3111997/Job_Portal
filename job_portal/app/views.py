from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from .models import *
from .forms import CandidateForm, SocialNetworkForm, ContactForm, JobPostingForm
from django.urls import reverse_lazy
from django.db.models import Q


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


class CandidateView(ListView):
    model = Candidate

    template_name = 'candidate.html'
    context_object_name='candidates'
    


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


class CandidateProfileView(TemplateView):
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
    template_name = 'employee.html'  # Make sure this template exists
    success_url = reverse_lazy('jobform')  # Redirect after successful form submission

    def form_valid(self, form):
        # Here you can perform additional actions if needed before saving
        form.save()  # Save the form data
        return super().form_valid(form)






def candidate_list(request):
    # Get the search parameters from the request
    keyword = request.GET.get('keyword', '')
    location = request.GET.get('location', '')
    gender = request.GET.get('gender', '')
    category_ids = request.GET.getlist('categories', [])
    radius = request.GET.get('radius', 50)
    experience = request.GET.getlist('experience', [])
    qualification_names = request.GET.getlist('qualifications', [])

    # Filter candidates based on the search parameters
    candidates = Candidate.objects.all()

    if keyword:
        candidates = candidates.filter(
            Q(fullname__icontains=keyword) |
            Q(job_title__icontains=keyword) |
            Q(description__icontains=keyword)
        )

    if location:
        candidates = candidates.filter(location__icontains=location)

    if gender:
        candidates = candidates.filter(gender=gender)

    if category_ids:
        candidates = candidates.filter(job_categories__id__in=category_ids).distinct()

    if experience:
        candidates = candidates.filter(experience__in=experience)

    if qualification_names:
        # Retrieve the qualification IDs from the database based on the names provided
        qualification_ids = Qualification.objects.filter(name__in=qualification_names).values_list('id', flat=True)
        candidates = candidates.filter(qualification__in=qualification_ids)

    context = {
        'candidates': candidates,
        'keyword': keyword,
        'location': location,
        'gender': gender,
        'categories': JobCategories.objects.all(),
        'selected_categories': category_ids,
        'radius': radius,
        'selected_experience': experience,
        'selected_qualifications': qualification_names,
        'experience_range': range(7),  # Example experience range
        'qualification_list': Qualification.objects.values_list('name', flat=True),  # Get qualification names from the database
    }

    return render(request, 'candidate.html', context)
