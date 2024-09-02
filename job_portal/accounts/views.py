from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .utils import authenticate,generate_token, send_password_reset_email
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import PasswordReset
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView

CustomUser = get_user_model()

class LoginView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate( email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': 'userdashboard' , "message":"SignIn Successfull, redirecting...."})
        else:
            return JsonResponse({'success': False, 'error': 'Wrong username or password. Please try again!!!'})

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

class ResetPassView(View):
    def post(self,request):
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'success': False, 'error': 'All fields are required.'})
        try:
            validate_email(email)  # Check if email is valid
        except ValidationError:
            return JsonResponse({'success': False, 'error': 'Invalid email address.'})

        user = CustomUser.objects.filter(email=email).first()

        if not user:
            return JsonResponse({'success': False, 'error': 'No user with Given Email.'})
        if PasswordReset.objects.filter(user=user).exists():
            return JsonResponse({'success': False, 'error': 'link already sent to email'})
        try:
            token = generate_token()
            PasswordReset.objects.create(user=user,token=token)
            reset_url = reverse('accounts:forgot_pass_confirm', kwargs={'token': token})
            reset_link = request.build_absolute_uri(reset_url)
            print(reset_link)
            # send_password_reset_email(user.email, reset_link)
            return JsonResponse({'success': True, 'message': 'Password reset Link sent to Email'})
        except:
            return JsonResponse({'success': False, 'error': 'Error while senting resetlink'})

class ResetPassConfirmView(View):
    template_name = 'passwordreset.html'

    def get(self,request,token):
        try:
            reset_token = PasswordReset.objects.get(token=token)
            if reset_token:
                form = SetPasswordForm(CustomUser)
                return render(request, self.template_name, {'form': form})
            else:
                return render(request, 'password_reset_invalid.html')
        except Exception as e:
            print(e)
            return render(request, 'password_reset_invalid.html')
        

    def post(self,request,token):
        try:
            form = SetPasswordForm(CustomUser, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data.get('new_password1')
                reset_token = PasswordReset.objects.get(token=token)
                user = reset_token.user
                user.set_password(new_password)
                user.save()
                #remove the passoword reset token
                reset_token.delete()
                return redirect('accounts:reset_pass_complete')  # Redirect to a success page
            else:
                return render(request, self.template_name, {'form': form})
        except Exception as e:
            print(e)
            return render(request, 'password_reset_invalid.html')

class ResetPassCompleteView(TemplateView):
    template_name = 'password_reset_complete.html'

