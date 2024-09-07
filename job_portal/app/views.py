from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, DeleteView
from django.views.generic.edit import FormView
from .models import Candidate, SocialNetwork, Contact, JobPosting, JobCategory, SavedJob
from django.views.generic import ListView
from .models import Qualification
from .forms import CandidateForm, SocialNetworkForm, ContactForm, JobPostingForm
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'userdashboard.html'
    login_url = '/'  # or use the name of your login URL pattern
    redirect_field_name = 'next'  # Default is 'next'


class AboutView(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = JobCategory.objects.all()
        context['jobs'] = JobPosting.objects.all()[:6]
        return context

class CategoryDetailView(TemplateView):
    template_name = 'jobs_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('pk')
        category = JobCategory.objects.get(pk=category_id)
        context['category'] = category
        context['jobs'] = category.jobposting_set.all()
        return context

class SaveJobView(LoginRequiredMixin, View):
    def post(self, request, job_id, candidate_id):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'You need to be logged in'})
        
        try:
            candidate = Candidate.objects.get(user=request.user)
        except Candidate.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'You need to be a candidate'})
        
        job = get_object_or_404(JobPosting, pk=job_id)
        candidate = get_object_or_404(Candidate, pk=candidate_id)

        saved_job, created = SavedJob.objects.get_or_create(candidate=candidate, job=job)

        if created:
            return JsonResponse({'status': 'success', 'message': 'Job saved successfully'})
        return JsonResponse({'status': 'exists', 'message': 'Job already saved'})


class SavedJobsView(LoginRequiredMixin, TemplateView):
    template_name = 'candidate_saved_jobs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        candidate = get_object_or_404(Candidate, user=user)
        saved_jobs = SavedJob.objects.filter(candidate=candidate)
        context['saved_jobs'] = saved_jobs
        return context


class DeleteSavedJobView(DeleteView):
    model = SavedJob
    template_name = "saved_jobs_delete_confirm.html"
    success_url = reverse_lazy('candidate_saved_jobs')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_postings'] = JobPosting.objects.all()  # Fetch all job postings
        return context
    

class EmployeeJobsView(TemplateView):
    template_name = 'employee.html'


class CandidateProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        candidate = None
        contact_instance = None
        
        if hasattr(user, 'candidate_profile'):
            candidate = user.candidate_profile
        
        if Contact.objects.filter(user=user).exists():
            contact_instance = Contact.objects.filter(user=user).first()

        candidate_form = CandidateForm(instance=candidate)
        contact_form = ContactForm(instance=contact_instance)
        return render(request, 'candidate_profile.html', {
            'candidate_form': candidate_form,
            'contact_form': contact_form,
        })

    def post(self, request, *args, **kwargs):
        try:
            candidate = request.user.candidate_profile
        except Candidate.DoesNotExist:
            candidate = None
        candidate_form = CandidateForm(request.POST, request.FILES, instance=candidate)
        contact_form = ContactForm(request.POST, instance=candidate.contacts.first() if candidate and candidate.contacts.exists() else None)

        if candidate_form.is_valid() and contact_form.is_valid():
            candidate_form.save()
            contact_form.save()
            return redirect('userdashboard')

        return render(request, 'candidate_profile.html', {
            'candidate_form': candidate_form,
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
        candidates = candidates.filter(job_category__id__in=category_ids).distinct()

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
        'categories': JobCategory.objects.all(),
        'selected_categories': category_ids,
        'radius': radius,
        'selected_experience': experience,
        'selected_qualifications': qualification_names,
        'experience_range': range(7),  # Example experience range
        'qualification_list': Qualification.objects.values_list('name', flat=True),  # Get qualification names from the database
    }

    return render(request, 'candidate.html', context)
