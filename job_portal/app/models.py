from django.db import models

    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    # Foreign key fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # Image field for featured image
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    # Basic information
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()

    # Choices
    JOB_TYPE_CHOICES = [
        ('freelance', 'Freelance'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    APPLY_TYPE_CHOICES = [
        ('online', 'Online'),
        ('inperson', 'Inperson'),
    ]
    SALARY_TYPE_CHOICES = [
        ('cheque', 'Cheque'),
        ('cash', 'Cash'),
    ]
    EXPERIENCE_CHOICES = [
        ('year1', '0-1 year'),
        ('year2', '2-3 years'),
    ]
    CAREER_LEVEL_CHOICES = [
        ('entry', 'Entry-Level'),
        ('senior', 'Senior-Level'),
    ]

    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    tag = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    apply_type = models.CharField(max_length=50, choices=APPLY_TYPE_CHOICES)
    external_url = models.URLField(blank=True, null=True)
    apply_email = models.EmailField(blank=True, null=True)
    salary_type = models.CharField(max_length=50, choices=SALARY_TYPE_CHOICES)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES)
    career_level = models.CharField(max_length=50, choices=CAREER_LEVEL_CHOICES)
    intro_video_url = models.URLField(blank=True, null=True)
    
    # Additional information
    application_deadline = models.DateField()
    friendly_address = models.CharField(max_length=255)

    def __str__(self):
        return self.job_title
