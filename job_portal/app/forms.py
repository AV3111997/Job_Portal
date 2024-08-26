from django import forms
from .models import JobPosting, Category, Qualification, Location

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            'featured_image': forms.ClearableFileInput(attrs={'multiple': False}),
            'photo': forms.ClearableFileInput(attrs={'multiple': False}),
            'external_url': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
            'apply_email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'intro_video_url': forms.URLInput(attrs={'placeholder': 'https://youtube.com/video'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['qualification'].queryset = Qualification.objects.all()
        self.fields['location'].queryset = Location.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        min_salary = cleaned_data.get('min_salary')
        max_salary = cleaned_data.get('max_salary')

        if min_salary and max_salary and min_salary > max_salary:
            self.add_error('max_salary', 'Max salary must be greater than or equal to min salary.')

        return cleaned_data
