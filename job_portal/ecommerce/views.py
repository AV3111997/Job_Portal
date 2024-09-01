from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class shopView(TemplateView):
    template_name = 'shop.html'
    