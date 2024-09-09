from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View, DeleteView, ListView
from django.views.generic.edit import FormView
from .forms import CandidateForm , ContactForm , CVForm
from .models import (
    Candidate,
    Contact,
    JobPosting,
    JobCategory,
    SavedJob,
    Employer,
    Qualification,
    Location,
    CV
)
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# Dashboard Views
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "userdashboard.html"
    login_url = "/"
    redirect_field_name = "next"


# Static Pages
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
        category = get_object_or_404(JobCategory, pk=category_id)
        context["category"] = category
        context["jobs"] = category.jobposting_set.all()
        return context


class SaveJobView(LoginRequiredMixin, View):
    def post(self, request, job_id, candidate_id):
        job = get_object_or_404(JobPosting, pk=job_id)
        candidate = get_object_or_404(Candidate, pk=candidate_id)
        saved_job, created = SavedJob.objects.get_or_create(candidate=candidate, job=job)

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

class ArticlesView(ListView):
    
    template_name = 'article_page.html'
    context_object_name = 'articles'  


class DeleteSavedJobView(DeleteView):
    model = SavedJob
    template_name = "saved_jobs_delete_confirm.html"
    success_url = reverse_lazy("candidate_saved_jobs")


# Job Management Views
class ManageJobsView(TemplateView):
    template_name = "manage_jobs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filters = {
            "employer_id": self.request.GET.get("employer"),
            "category_id": self.request.GET.get("category"),
            "min_salary__gte": self.request.GET.get("min_salary"),
            "max_salary__lte": self.request.GET.get("max_salary"),
            "job_type": self.request.GET.get("job_type"),
            "experience": self.request.GET.get("experience"),
            "status": self.request.GET.get("status"),
        }
        # Remove filters with None values
        filters = {k: v for k, v in filters.items() if v}

        job_postings = JobPosting.objects.filter(**filters)
        paginator = Paginator(job_postings, 10)
        page_obj = paginator.get_page(self.request.GET.get("page", 1))

        context.update({
            "job_postings": page_obj,
            "page_obj": page_obj,
            "employers": Employer.objects.all(),
            "categories": JobCategory.objects.all(),
            "job_types": JobPosting.JOB_TYPE_CHOICES,
            "experiences": JobPosting.EXPERIENCE_CHOICES,
            "statuses": JobPosting.STATUS_CHOICES,
        })
        return context


# Candidate Views
def candidate_list(request):
    keyword = request.GET.get("keyword", "")
    location = request.GET.get("location", "")
    gender = request.GET.get("gender", "")
    category_ids = request.GET.getlist("categories", [])
    experience = request.GET.getlist("experience", [])
    qualification_names = request.GET.getlist("qualifications", [])

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
        "selected_experience": experience,
        "selected_qualifications": qualification_names,
        "experience_range": range(7),
        "qualification_list": Qualification.objects.all(),
    }
    return render(request, "candidate.html", context)


def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched", "")
        location_id = request.POST.get("location", "")
        jobs = JobPosting.objects.all()

        if searched:
            jobs = jobs.filter(Q(job_title__icontains=searched))

        if location_id:
            location = get_object_or_404(Location, id=location_id)
            jobs = jobs.filter(location=location)

        context = {
            "searched": searched,
            "searched_jobs": jobs,
            "location": location,
        }
        return render(request, "Searched_jobs_result.html", context)
    return redirect("/")
