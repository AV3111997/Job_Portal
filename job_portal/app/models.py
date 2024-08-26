from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobCategories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    AGE_CATEGORY_CHOICES = [
        ('18-20', '18-20'),
        ('20-25', '20-25'),
        ('25-30', '25-30'),
        ('30-35', '30-35'),
        ('35-40', '35-40'),
    ]

    EXPERIENCE_CHOICES = [
        ('0', 'Fresher'),
        ('1', '1 Year'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5', '5 Years'),
        ('6', '6 Years'),
    ]

    SALARY_TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Daily', 'Daily'),
        ('Hourly', 'Hourly'),
        ('Yearly', 'Yearly'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    fullname = models.CharField(max_length=100, verbose_name='Full Name')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male', verbose_name='Gender')
    age = models.CharField(max_length=20, choices=AGE_CATEGORY_CHOICES, default='18-20', verbose_name='Age')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Phone')
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Qualification')
    languages = models.ManyToManyField(Language, verbose_name='Languages')
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, default='Fresher', verbose_name='Experience')
    salary_type = models.CharField(max_length=50, choices=SALARY_TYPE_CHOICES, default='Monthly', verbose_name='Salary Type')
    salary = models.CharField(max_length=50, verbose_name='Salary')
    job_categories = models.ManyToManyField(JobCategories, verbose_name='Categories')
    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    description = models.TextField()

class SocialNetwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_networks')
    name = models.CharField(max_length=100)
    url_pattern = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    address = models.CharField(max_length=200, verbose_name='Address')
    location = models.CharField(max_length=100, verbose_name='Location')
