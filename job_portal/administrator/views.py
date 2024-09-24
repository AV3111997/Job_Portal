from django.shortcuts import render, redirect
from app.models import Employer, Candidate, Language, Location, JobCategory, ProfessionalSkill
from app.forms import LanguageForm, LocationForm, JobCategoryForm, ProfessionalSkillForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class EmployerListView(ListView):
    model = Employer
    template_name = 'employers/list.html' 
    context_object_name = 'employers'  

class EmployerDeleteView(DeleteView):
    model = Employer
    template_name = 'employers/delete.html'
    success_url = reverse_lazy('employer_list')


class CandidateListView(ListView):
    model = Candidate
    template_name = 'candidates/list.html' 
    context_object_name = 'candidatelist'  

class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'employers/delete.html'
    success_url = reverse_lazy('employer_list')


class LanguageListView(ListView):
    model = Language
    template_name = 'languages/list.html'
    context_object_name = 'languages'

class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'languages/create.html'
    success_url = reverse_lazy('language_list')

class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'languages/create.html'
    success_url = reverse_lazy('language_list')

class LanguageDeleteView(DeleteView):
    model = Language
    success_url = reverse_lazy('language_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
    
class LocationListView(ListView):
    model = Location
    template_name = 'locations/list.html'
    context_object_name = 'locations'

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'locations/create.html'
    success_url = reverse_lazy('location_list')

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'locations/create.html'
    success_url = reverse_lazy('location_list')

class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'locations/delete.html'
    success_url = reverse_lazy('location_list')


class JobCategoryListView(ListView):
    model = JobCategory
    template_name = 'job_categorys/list.html'
    context_object_name = 'job_categorys'

class JobCategoryCreateView(CreateView):
    model = JobCategory
    form_class = JobCategoryForm
    template_name = 'job_categorys/create.html'
    success_url = reverse_lazy('jobcategory_list')

class JobCategoryUpdateView(UpdateView):
    model = JobCategory
    form_class = JobCategoryForm
    template_name = 'job_categorys/create.html'
    success_url = reverse_lazy('jobcategory_list')

class JobCategoryDeleteView(DeleteView):
    model = JobCategory
    template_name = 'job_categorys/delete.html'
    success_url = reverse_lazy('jobcategory_list')

class ProfessionalSkillListView(ListView):
    model = ProfessionalSkill
    template_name = 'professional_skills/list.html'
    context_object_name = 'professional_skill'

class ProfessionalSkillCreateView(CreateView):
    model = ProfessionalSkill
    form_class = ProfessionalSkillForm
    template_name = 'professional_skills/create.html'
    success_url = reverse_lazy('professionalskill_list')

class ProfessionalSkillUpdateView(UpdateView):
    model = ProfessionalSkill
    form_class = ProfessionalSkillForm
    template_name = 'professional_skills/create.html'
    success_url = reverse_lazy('professionalskill_list')

class ProfessionalSkillDeleteView(DeleteView):
    model = ProfessionalSkill
    template_name = 'professional_skills/delete.html'
    success_url = reverse_lazy('professionalskill_list')