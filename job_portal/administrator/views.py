from django.shortcuts import render, redirect
from app.models import Employer,Candidate
from app.forms import LanguageForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import Employer, Language
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
