from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html')

class FAQView(TemplateView):
    template_name = 'faq.html' 

class PricingView(TemplateView):
    template_name = 'pricing.html' 

def candidate_view(request):
    return render(request, 'candidate.html')

def Joblist_view(request):
    return render(request,'findjoblist.html')

def Employerslist_view(request):
    return render(request,'employerslist.html')