from django.shortcuts import render
from app.models import Employer,Candidate
from django.urls import reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.edit import DeleteView


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