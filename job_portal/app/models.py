from django.db import models
from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.


class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default="default-icon")

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name



class Candidate(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    AGE_CATEGORY_CHOICES = [
        ("18-20", "18-20"),
        ("20-25", "20-25"),
        ("25-30", "25-30"),
        ("30-35", "30-35"),
        ("35-40", "35-40"),
    ]

    EXPERIENCE_CHOICES = [
        ("0", "Fresher"),
        ("1", "1 Year"),
        ("2", "2 Years"),
        ("3", "3 Years"),
        ("4", "4 Years"),
        ("5", "5 Years"),
        ("6", "6 Years"),
    ]

    SALARY_TYPE_CHOICES = [
        ("Monthly", "Monthly"),
        ("Weekly", "Weekly"),
        ("Daily", "Daily"),
        ("Hourly", "Hourly"),
        ("Yearly", "Yearly"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="candidate_profile"
    )
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )
    fullname = models.CharField(max_length=100, verbose_name="Full Name")
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name="Date of Birth"
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default="Male", verbose_name="Gender"
    )
    age = models.CharField(
        max_length=20, choices=AGE_CATEGORY_CHOICES, default="18-20", verbose_name="Age"
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone")
    qualification = models.ForeignKey(
        Qualification,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Qualification",
    )
    languages = models.ManyToManyField(Language, verbose_name="Languages")
    experience = models.CharField(
        max_length=50,
        choices=EXPERIENCE_CHOICES,
        default="Fresher",
        verbose_name="Experience",
    )
    salary_type = models.CharField(
        max_length=50,
        choices=SALARY_TYPE_CHOICES,
        default="Monthly",
        verbose_name="Salary Type",
    )
    salary = models.CharField(max_length=50, verbose_name="Salary")
    job_category = models.ManyToManyField(
        JobCategory,
        verbose_name="category",
        blank=True,
    )
    job_title = models.CharField(max_length=100, verbose_name="Job Title")
    description = models.TextField()


class SocialNetwork(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="social_networks"
    )
    name = models.CharField(max_length=100)
    url_pattern = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class CandidateContact(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="candidate_contacts"
    )
    address = models.CharField(max_length=200, verbose_name="address")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="candidate_contacts")


class Employer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="employers"
    )
    employer_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    founded_date = models.DateField(
        null=True,
        blank=True,
    )
    logo = models.ImageField(upload_to="employer_logos/")
    cover_photo = models.ImageField(upload_to="employer_coverphoto/")
    company_size = models.CharField(max_length=20)
    introduction_video_url = models.URLField(max_length=200)
    description = models.CharField(max_length=255)
    profile_url = models.URLField(max_length=200)
    is_open_job = models.BooleanField(default=True)

    def __str__(self):
        return self.employer_name

class EmployerContact(models.Model):
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, related_name="employer_contacts"
    )
    address = models.CharField(max_length=200, verbose_name="Address")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="employer_contacts")

class ProfilePhoto(models.Model):
    employer = models.ForeignKey(
        Employer, related_name="profile_photos", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="employer_profilephoto/")


class Member(models.Model):
    employer = models.ForeignKey(
        Employer, related_name="members", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)


class JobPosting(models.Model):
    # Foreign key fields
    employer = models.ForeignKey(
        Employer, related_name="job_postings", on_delete=models.CASCADE
    )
    job_category = models.ManyToManyField(
        JobCategory, verbose_name="job_category", blank=True
    )
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # Image field for featured image
    featured_image = models.ImageField(
        upload_to="featured_images/", blank=True, null=True
    )
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)

    # Basic information
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()

    # Choices
    JOB_TYPE_CHOICES = [
        ("freelance", "Freelance"),
        ("contract", "Contract"),
        ("full-time", "Full Time"),
        ("part-time", "Part Time"),
        ("internship", "Internship"),
    ]
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]
    URGENCY_LEVEL_CHOICES = [
        ("Urgent", "Urgent"),
        ("Normal", "Normal"),
        ("Immediate", "Immediate"),
    ]
    APPLY_TYPE_CHOICES = [
        ("online", "Online"),
        ("inperson", "Inperson"),
    ]
    STATUS_CHOICES = [
        ("open", "Open"),
        ("filled", "Filled"),
        ("draft", "Draft"),
    ]
    SALARY_TYPE_CHOICES = [
        ("Monthly", "Monthly"),
        ("Weekly", "Weekly"),
        ("Daily", "Daily"),
        ("Hourly", "Hourly"),
        ("Yearly", "Yearly"),
    ]
    EXPERIENCE_CHOICES = [
        ("0", "Fresher"),
        ("1", "1 Year"),
        ("2", "2 Years"),
        ("3", "3 Years"),
        ("4", "4 Years"),
        ("5", "5 Years"),
        ("6", "6 Years"),
    ]
    CAREER_LEVEL_CHOICES = [
        ("entry", "Entry-Level"),
        ("senior", "Senior-Level"),
    ]

    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    apply_type = models.CharField(max_length=50, choices=APPLY_TYPE_CHOICES)
    urgency_level = models.CharField(max_length=10, choices=URGENCY_LEVEL_CHOICES)
    external_url = models.URLField(blank=True, null=True)
    apply_email = models.EmailField(blank=True, null=True)
    salary_type = models.CharField(
        max_length=50, choices=SALARY_TYPE_CHOICES, default="Monthly"
    )
    min_salary = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True
    )
    max_salary = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True
    )
    experience = models.CharField(
        max_length=50, choices=EXPERIENCE_CHOICES, default="Fresher"
    )
    career_level = models.CharField(max_length=50, choices=CAREER_LEVEL_CHOICES)
    intro_video_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="open")

    # Additional information
    application_deadline = models.DateField(null=True, blank=True)
    friendly_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.job_title} at {self.employer.employer_name}"


class SavedJob(models.Model):
    candidate = models.ForeignKey(
        Candidate, related_name="candidate", on_delete=models.CASCADE
    )
    job = models.ForeignKey(JobPosting, related_name="job", on_delete=models.CASCADE)


class CV(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="candidate_cv", on_delete=models.CASCADE)
    file = models.FileField(upload_to="cvs/")
