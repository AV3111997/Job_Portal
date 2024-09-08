from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, DeleteView
from django.views.generic.edit import FormView
from .models import (
    Candidate,
    Contact,
    JobPosting,
    JobCategory,
    SavedJob,
    Employer,
    Qualification,
    Location,
)
from django.views.generic import ListView
from .forms import CandidateForm, ContactForm, JobPostingForm
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

# Create your views here.


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "userdashboard.html"

    login_url = "/"  # or use the name of your login URL pattern
    redirect_field_name = "next"  # Default is 'next'


class AboutView(TemplateView):
    template_name = "about.html"


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()
        context["categories"] = JobCategory.objects.all()
        context["jobs"] = JobPosting.objects.all()[:6]
        return context


class CategoryDetailView(TemplateView):
    template_name = "jobs_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("pk")
        category = JobCategory.objects.get(pk=category_id)
        context["category"] = category
        context["jobs"] = category.jobposting_set.all()
        return context


class SaveJobView(LoginRequiredMixin, View):
    def post(self, request, job_id, candidate_id):
        # if not request.user.is_authenticated:
        #     return JsonResponse({'status': 'error', 'message': 'You need to be logged in'})

        # try:
        #     candidate = Candidate.objects.get(user=request.user)
        # except Candidate.DoesNotExist:
        #     return JsonResponse({'status': 'error', 'message': 'You need to be a candidate'})

        job = get_object_or_404(JobPosting, pk=job_id)
        candidate = get_object_or_404(Candidate, pk=candidate_id)

        saved_job, created = SavedJob.objects.get_or_create(
            candidate=candidate, job=job
        )

        if created:
            return JsonResponse(
                {"status": "success", "message": "Job saved successfully"}
            )
        return JsonResponse({"status": "exists", "message": "Job already saved"})


class SavedJobsView(LoginRequiredMixin, TemplateView):
    template_name = "candidate_saved_jobs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        candidate = get_object_or_404(Candidate, user=user)
        saved_jobs = SavedJob.objects.filter(candidate=candidate)
        context["saved_jobs"] = saved_jobs
        return context


class DeleteSavedJobView(DeleteView):
    model = SavedJob
    template_name = "saved_jobs_delete_confirm.html"
    success_url = reverse_lazy("candidate_saved_jobs")


class ArticlesView(TemplateView):
    template_name = "article_page.html"


class FAQView(TemplateView):
    template_name = "faq.html"


class PricingView(TemplateView):
    template_name = "pricing.html"


class JobDetailsView(TemplateView):
    template_name = "job_details.html"


class CandidateView(ListView):
    model = Candidate

    template_name = "candidate.html"
    context_object_name = "candidates"


class EmployersListView(TemplateView):
    template_name = "employerslist.html"


class JobListView(TemplateView):
    template_name = "findjoblist.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class ProfileView(TemplateView):
    template_name = "profile.html"


class TermView(TemplateView):
    template_name = "terms.html"


class AppliedJobsView(TemplateView):
    template_name = "applied_jobs.html"


class ApplicantsJobsView(TemplateView):
    template_name = "applicants_jobs.html"


class ManageJobsView(TemplateView):
    template_name = "manage_jobs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get filter values from request parameters
        employer_id = self.request.GET.get("employer")
        category_id = self.request.GET.get("category")
        min_salary = self.request.GET.get("min_salary")
        max_salary = self.request.GET.get("max_salary")
        job_type = self.request.GET.get("job_type")
        experience = self.request.GET.get("experience")
        status = self.request.GET.get("status")

        # Start with all job postings
        job_postings = JobPosting.objects.all()

        # Apply filters if available
        if employer_id:
            job_postings = job_postings.filter(employer_id=employer_id)

        if category_id:
            job_postings = job_postings.filter(category_id=category_id)

        if min_salary:
            job_postings = job_postings.filter(min_salary__gte=min_salary)

        if max_salary:
            job_postings = job_postings.filter(max_salary__lte=max_salary)

        if job_type:
            job_postings = job_postings.filter(job_type=job_type)

        if experience:
            job_postings = job_postings.filter(experience=experience)

        if status:
            job_postings = job_postings.filter(status=status)

        # Pagination
        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(job_postings, 10)  # Show 10 job postings per page
        page_obj = paginator.get_page(page_number)

        # Add job postings and filter options to context
        context["job_postings"] = page_obj  # Pass paginated object to template
        context["page_obj"] = page_obj
        context["employers"] = Employer.objects.all()
        context["categories"] = JobCategory.objects.all()
        context["job_types"] = JobPosting.JOB_TYPE_CHOICES
        context["experiences"] = JobPosting.EXPERIENCE_CHOICES
        context["statuses"] = JobPosting.STATUS_CHOICES

        return context


class EmployeeJobsView(TemplateView):
    template_name = "employee.html"


class CandidateProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        candidate = None
        contact_instance = None

        if hasattr(user, "candidate_profile"):
            candidate = user.candidate_profile
            if candidate.contacts.exists():
                contact_instance = candidate.contacts.first()

        candidate_form = CandidateForm(instance=candidate)
        contact_form = (
            ContactForm(instance=contact_instance)
            if contact_instance
            else ContactForm()
        )

        return render(
            request,
            "candidate_profile.html",
            {
                "candidate_form": candidate_form,
                "contact_form": contact_form,
            },
        )

    def post(self, request, *args, **kwargs):
        user = request.user
        candidate = user.candidate_profile

        candidate_form = CandidateForm(request.POST, request.FILES, instance=candidate)

        contact_instance = None
        if candidate.contacts.exists():
            contact_instance = candidate.contacts.first()

        contact_form = ContactForm(request.POST, instance=contact_instance)

        if candidate_form.is_valid() and contact_form.is_valid():
            candidate = candidate_form.save()

            contact = contact_form.save(commit=False)
            contact_data = contact_form.cleaned_data
            contact = Contact(
                address=contact_data["address"],
                location=contact_data["location"],
                candidate=candidate,
            )
            contact.save()

            return redirect("userdashboard")

        return render(
            request,
            "candidate_profile.html",
            {
                "candidate_form": candidate_form,
                "contact_form": contact_form,
            },
        )


class JobPostingCreateView(FormView):
    template_name = "jobposting.html"
    form_class = JobPostingForm
    success_url = reverse_lazy("manage_jobs")

    def get(self, request, *args, **kwargs):
        user = request.user
        employer = getattr(user, "employers", None)

        if employer:
            jobposting_form = self.form_class()
            return render(
                request,
                self.template_name,
                {
                    "jobposting_form": jobposting_form,
                },
            )
        else:
            messages.error(request, "You must have an employer profile to post a job.")
            return redirect("jobpost_form")

    def post(self, request, *args, **kwargs):
        user = request.user
        employer = getattr(user, "employers", None)

        if employer:
            jobposting_form = self.form_class(request.POST, request.FILES)

            if jobposting_form.is_valid():
                job_posting = jobposting_form.save(commit=False)
                job_posting.employer = employer
                job_posting.save()

                messages.success(request, "Job posting created successfully!")
                return redirect("jobpost_form")

        else:
            messages.error(request, "You must have an employer profile to post a job.")
            return redirect("jobpost_form")

        return render(
            request,
            self.template_name,
            {
                "jobposting_form": jobposting_form,
            },
        )


class JobPostingUpdateView(FormView):
    model = JobPosting
    form_class = JobPostingForm
    template_name = "jobposting.html"
    success_url = reverse_lazy("manage_jobs")

    def get_object(self, queryset=None):
        user = self.request.user
        employer = getattr(user, "employers", None)

        job_posting = get_object_or_404(
            JobPosting, pk=self.kwargs["pk"], employer=employer
        )
        return job_posting

    def form_valid(self, form):
        messages.success(self.request, "Job posting updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating the job posting.")
        return super().form_invalid(form)


def candidate_list(request):
    # Get the search parameters from the request
    keyword = request.GET.get("keyword", "")
    location = request.GET.get("location", "")
    gender = request.GET.get("gender", "")
    category_ids = request.GET.getlist("categories", [])
    radius = request.GET.get("radius", 50)
    experience = request.GET.getlist("experience", [])
    qualification_names = request.GET.getlist("qualifications", [])

    # Filter candidates based on the search parameters
    candidates = Candidate.objects.all()

    if keyword:
        candidates = candidates.filter(
            Q(fullname__icontains=keyword)
            | Q(job_title__icontains=keyword)
            | Q(description__icontains=keyword)
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
        qualification_ids = Qualification.objects.filter(
            name__in=qualification_names
        ).values_list("id", flat=True)
        candidates = candidates.filter(qualification__in=qualification_ids)

    context = {
        "candidates": candidates,
        "keyword": keyword,
        "location": location,
        "gender": gender,
        "categories": JobCategory.objects.all(),
        "selected_categories": category_ids,
        "radius": radius,
        "selected_experience": experience,
        "selected_qualifications": qualification_names,
        "experience_range": range(7),  # Example experience range
        "qualification_list": Qualification.objects.all(),  # Get qualification names from the database
    }

    return render(request, "candidate.html", context)


def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched", "")
        location_id = request.POST.get("location", "")
        jobs = JobPosting.objects.all()
        if searched:
            jobs = jobs.filter(Q(job_title__icontains=searched))
        location = None
        if location_id:
            try:
                location = Location.objects.get(id=location_id)
                jobs = jobs.filter(location=location)
            except Location.DoesNotExist:
                location = None
        context = {
            "searched": searched,
            "searched_jobs": jobs,
            "location": location,
        }
        return render(request, "Searched_jobs_result.html", context)
    else:
        return redirect("/")
