from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .utils import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import CustomUser
from django.shortcuts import redirect




class LoginView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate( email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': True, 'redirect_url': 'userdashboard'})
        else:
            return JsonResponse({'status': False, 'message': 'Invalid credentials'})


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        user_type = request.POST.get('userType')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if not email or not password or not confirmpassword or not user_type:
            return JsonResponse({'success': False, 'error': 'All fields are required.'})

        if password != confirmpassword:
            return JsonResponse({'success': False, 'error': 'Passwords do not match.'})

        try:
            validate_email(email)  # Check if email is valid
        except ValidationError:
            return JsonResponse({'success': False, 'error': 'Invalid email address.'})

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'Email is already in use.'})
        
                # Create new user
        user = CustomUser.objects.create_user(username=email,email=email, password=password,user_type=user_type)
        user.save()

        return JsonResponse({'success': True, 'message': 'User registered successfully.'})
