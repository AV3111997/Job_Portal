from django import forms
from .models import Candidate, SocialNetwork, Contact

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'profile_image', 'fullname', 'date_of_birth', 'gender', 'age', 'email',
            'phone_number', 'qualification', 'languages', 'experience', 'salary_type',
            'salary', 'job_categories', 'job_title', 'description'
        ]
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'qualification': forms.Select(attrs={'class': 'form-control'}),
            'languages': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'experience': forms.Select(attrs={'class': 'form-control'}),
            'salary_type': forms.Select(attrs={'class': 'form-control'}),
            'job_categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        fields = '__all__'
        widgets = {
            'url_pattern': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SocialNetworkForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
