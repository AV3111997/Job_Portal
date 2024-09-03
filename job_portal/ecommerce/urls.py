from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shopView.as_view(), name='shop'),
]