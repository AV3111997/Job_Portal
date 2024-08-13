from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('candidate', views.candidate_view, name='candidate'),
    path('terms/', views.terms_view, name='terms'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),

]