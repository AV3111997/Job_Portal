from django import forms
<<<<<<< HEAD
from .models import Candidate, SocialNetwork, Contact, JobPosting, JobCategory, Qualification, Location, Employer , CV
=======
from .models import (
    Candidate,
    SocialNetwork,
    Contact,
    JobPosting,
    JobCategory,
    Qualification,
    Location,
    Employer,
)
>>>>>>> origin/main


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            "profile_image",
            "fullname",
            "date_of_birth",
            "gender",
            "age",
            "email",
            "phone_number",
            "qualification",
            "languages",
            "experience",
            "salary_type",
            "salary",
            "job_category",
            "job_title",
            "description",
        ]
        widgets = {
            "profile_image": forms.FileInput(
                attrs={"class": "form-control candidate_profile_input"}
            ),
            "fullname": forms.TextInput(attrs={"class": " form-control"}),
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.TextInput(attrs={"class": "form-control"}),
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "age": forms.Select(attrs={"class": "form-control"}),
            "qualification": forms.Select(attrs={"class": "form-control"}),
            "languages": forms.SelectMultiple(attrs={"class": "form-control"}),
            "experience": forms.Select(attrs={"class": "form-control"}),
            "salary_type": forms.Select(attrs={"class": "form-control"}),
            "job_category": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["address", "location"]
        widgets = {
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = "__all__"
        widgets = {
            "job_description": forms.Textarea(attrs={"rows": 4}),
            "application_deadline": forms.DateInput(attrs={"type": "date"}),
            "featured_image": forms.ClearableFileInput(attrs={"multiple": False}),
            "photo": forms.ClearableFileInput(attrs={"multiple": False}),
            "external_url": forms.URLInput(
                attrs={"placeholder": "https://example.com"}
            ),
            "apply_email": forms.EmailInput(
                attrs={"placeholder": "example@example.com"}
            ),
            "intro_video_url": forms.URLInput(
                attrs={"placeholder": "https://youtube.com/video"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set queryset for employer, category, qualification, and location
        self.fields["employer"].queryset = Employer.objects.all()
        self.fields["category"].queryset = JobCategory.objects.all()
        self.fields["qualification"].queryset = Qualification.objects.all()
        self.fields["location"].queryset = Location.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        min_salary = cleaned_data.get("min_salary")
        max_salary = cleaned_data.get("max_salary")

        if min_salary and max_salary and min_salary > max_salary:
            self.add_error(
                "max_salary", "Max salary must be greater than or equal to min salary."
            )

        return cleaned_data


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'file']
