from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('candidate', views.candidate_view, name='candidate'),
]