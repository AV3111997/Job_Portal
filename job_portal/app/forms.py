from django import forms
from .models import (
    Candidate,
    SocialNetwork,
    CandidateContact,
    EmployerContact,
    JobPosting,
    JobCategory,
    Qualification,
    Location,
    Employer,
    CV,
)

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = [
            'employer_name',
            'location',
            'email',
            'phone_no',
            'website',
            'founded_date',
            'logo',
            'cover_photo',
            'company_size',
            'introduction_video_url',
            'description',
            'profile_url',
            'is_open_job',
        ]
        widgets = {
            'founded_date': forms.DateInput(attrs={'type': 'date'}),
            'logo': forms.ClearableFileInput(attrs={'multiple': False}),
            'cover_photo': forms.ClearableFileInput(attrs={'multiple': False}),
            'introduction_video_url': forms.URLInput(attrs={'placeholder': 'Enter YouTube or Video URL'}),
            'profile_url': forms.URLInput(attrs={'placeholder': 'Enter your company website URL'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


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


class CandidateContactForm(forms.ModelForm):
    class Meta:
        model = CandidateContact
        fields = ["address", "location"]
        widgets = {
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(CandidateContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class EmployerContactForm(forms.ModelForm):
    class Meta:
        model = EmployerContact
        fields = ["address", "location"]
        widgets = {
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployerContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = "__all__"
        widgets = {
            "job_description": forms.Textarea(attrs={"class": "form-control"}),
            "application_deadline": forms.DateInput(attrs={"class": "form-control", "type": "date" }),
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "form-control", "multiple": False}
            ),
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control", "multiple": False}
            ),
            "external_url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "https://example.com"}
            ),
            "apply_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "example@example.com"}
            ),
            "intro_video_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://youtube.com/video",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set queryset for employer, category, qualification, and location
        self.fields["employer"].queryset = Employer.objects.all()
        self.fields["job_category"].queryset = JobCategory.objects.all()
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

    def __init__(self, *args, **kwargs):
        super(JobPostingForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ["file"]
