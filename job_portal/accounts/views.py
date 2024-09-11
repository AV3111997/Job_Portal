from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .utils import authenticate, generate_token, send_password_reset_email
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import PasswordReset
from django.urls import reverse
from app.models import Candidate, Employer
from django.views.generic import TemplateView
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordConfirmationForm

User = get_user_model()


class LoginView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    "success": True,
                    "redirect_url": reverse("home"),
                    "message": "SignIn Successfull, redirecting....",
                }
            )
        else:
            return JsonResponse(
                {
                    "success": False,
                    "error": "Wrong username or password. Please try again!!!",
                }
            )


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        user_type = request.POST.get("userType")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        if not email or not password or not confirmpassword or not user_type:
            return JsonResponse({"success": False, "error": "All fields are required."})

        if password != confirmpassword:
            return JsonResponse({"success": False, "error": "Passwords do not match."})

        try:
            validate_email(email)  # Check if email is valid
        except ValidationError:
            return JsonResponse({"success": False, "error": "Invalid email address."})

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "Email is already in use."})

            # Create new user
        user = User.objects.create_user(
            username=email, email=email, password=password, user_type=user_type
        )
        user.save()

        if user_type == "candidate":
            Candidate.objects.create(
                user=user,
                email=user.email,
            )

        elif user_type == "employer":
            Employer.objects.create(
                user=user,
                email=user.email,
            )

        return JsonResponse(
            {
                "success": True,
                "message": "User registered successfully.",
            }
        )


class ResetPassView(View):
    def post(self, request):
        email = request.POST.get("email")
        if not email:
            return JsonResponse({"success": False, "error": "All fields are required."})
        try:
            validate_email(email)  # Check if email is valid
        except ValidationError:
            return JsonResponse({"success": False, "error": "Invalid email address."})

        user = User.objects.filter(email=email).first()

        if not user:
            return JsonResponse(
                {"success": False, "error": "No user with Given Email."}
            )
        if PasswordReset.objects.filter(user=user).exists():
            return JsonResponse(
                {"success": False, "error": "link already sent to email"}
            )
        try:
            token = generate_token()
            PasswordReset.objects.create(user=user, token=token)
            reset_url = reverse("accounts:forgot_pass_confirm", kwargs={"token": token})
            reset_link = request.build_absolute_uri(reset_url)
            print(reset_link)
            # send_password_reset_email(user.email, reset_link)
            return JsonResponse(
                {"success": True, "message": "Password reset Link sent to Email"}
            )
        except:
            return JsonResponse(
                {"success": False, "error": "Error while senting resetlink"}
            )


class ResetPassConfirmView(View):
    template_name = "passwordreset.html"

    def get(self, request, token):
        try:
            reset_token = PasswordReset.objects.get(token=token)
            if reset_token:
                form = SetPasswordForm(User)
                return render(request, self.template_name, {"form": form})
            else:
                return render(request, "password_reset_invalid.html")
        except Exception as e:
            print(e)
            return render(request, "password_reset_invalid.html")

    def post(self, request, token):
        try:
            form = SetPasswordForm(User, request.POST)
            if form.is_valid():
                new_password = form.cleaned_data.get("new_password1")
                reset_token = PasswordReset.objects.get(token=token)
                user = reset_token.user
                user.set_password(new_password)
                user.save()
                # remove the passoword reset token
                reset_token.delete()
                return redirect(
                    "accounts:reset_pass_complete"
                )  # Redirect to a success page
            else:
                return render(request, self.template_name, {"form": form})
        except Exception as e:
            print(e)
            return render(request, "password_reset_invalid.html")


class ResetPassCompleteView(TemplateView):
    template_name = "password_reset_complete.html"


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'profile_confirm_delete.html'
    success_url = reverse_lazy('home')  # Redirect after successful deletion

    def get_object(self, queryset=None):
        # Override to get the current logged-in user
        return self.request.user
    
    def get(self,request):
        form = PasswordConfirmationForm()
        context = {
            'form':form,
            'object':self.get_object(),
        }
        return render(request, self.template_name, context)
    

    
    def post(self, request):
        form = PasswordConfirmationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = self.get_object()
            if user.check_password(password):
                return self.delete(request)
            else:
                form.add_error('password', 'Incorrect password.')

        context = {
            'form':form,
            'object':self.get_object(),
        }
        return render(request, self.template_name,context)
        

    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        logout(request)  # Log the user out after deletion
        return response
    

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'

    def form_valid(self, form):
        # Call the parent class's form_valid method to save the form
        response = super().form_valid(form)
        # Add a success message
        messages.success(self.request, 'Your password has been changed successfully.')
        return response

    def get_success_url(self):
        # Redirect to the same page to show the success message
        return reverse_lazy('accounts:password_change')