from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from .views import ProfileDeleteView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-pass/', ResetPassView.as_view(), name='reset-pass'),
    path('reset-pass-confirm/<token>/',ResetPassConfirmView.as_view(),name='forgot_pass_confirm'),
    path('reset-pass-complete/',ResetPassCompleteView.as_view(),name='reset_pass_complete'),
    path('profile-delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('password_change/',CustomPasswordChangeView.as_view(),name='password_change'),
]
