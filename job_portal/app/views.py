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

def terms_view(request):
    return render(request, 'terms.html')

def contact_view(request):
    return render(request, 'contact.html')

def profile_view(request):
    return render(request, 'profile.html')