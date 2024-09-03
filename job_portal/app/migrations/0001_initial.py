# Generated by Django 5.0.8 on 2024-09-02 07:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(default='default-icon', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('founded_date', models.DateField()),
                ('logo', models.ImageField(upload_to='employer_logos/')),
                ('cover_photo', models.ImageField(upload_to='employer_coverphoto/')),
                ('company_size', models.CharField(max_length=20)),
                ('introduction_video_url', models.URLField()),
                ('description', models.CharField(max_length=255)),
                ('profile_url', models.URLField()),
                ('is_open_job', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.employer')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='employer_profilephoto/')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_photos', to='app.employer')),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='featured_images/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('job_title', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('job_type', models.CharField(choices=[('freelance', 'Freelance'), ('contract', 'Contract'), ('full-time', 'Full Time'), ('part-time', 'Part Time'), ('internship', 'Internship')], max_length=50)),
                ('tag', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('apply_type', models.CharField(choices=[('online', 'Online'), ('inperson', 'Inperson')], max_length=50)),
                ('urgency_level', models.CharField(choices=[('Urgent', 'Urgent'), ('Normal', 'Normal'), ('Immidiate', 'Immidiate')], max_length=10)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('apply_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('salary_type', models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Hourly', 'Hourly'), ('Yearly', 'Yearly')], max_length=50)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('experience', models.CharField(choices=[('0', 'Fresher'), ('1', '1 Year'), ('2', '2 Years'), ('3', '3 Years'), ('4', '4 Years'), ('5', '5 Years'), ('6', '6 Years')], max_length=50)),
                ('career_level', models.CharField(choices=[('entry', 'Entry-Level'), ('senior', 'Senior-Level')], max_length=50)),
                ('intro_video_url', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('filled', 'Filled')], max_length=50)),
                ('application_deadline', models.DateField()),
                ('friendly_address', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobcategory')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='app.employer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('fullname', models.CharField(max_length=100, verbose_name='Full Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=20, verbose_name='Gender')),
                ('age', models.CharField(choices=[('18-20', '18-20'), ('20-25', '20-25'), ('25-30', '25-30'), ('30-35', '30-35'), ('35-40', '35-40')], default='18-20', max_length=20, verbose_name='Age')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone')),
                ('experience', models.CharField(choices=[('0', 'Fresher'), ('1', '1 Year'), ('2', '2 Years'), ('3', '3 Years'), ('4', '4 Years'), ('5', '5 Years'), ('6', '6 Years')], default='Fresher', max_length=50, verbose_name='Experience')),
                ('salary_type', models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Hourly', 'Hourly'), ('Yearly', 'Yearly')], default='Monthly', max_length=50, verbose_name='Salary Type')),
                ('salary', models.CharField(max_length=50, verbose_name='Salary')),
                ('job_title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_profile', to=settings.AUTH_USER_MODEL)),
                ('job_category', models.ManyToManyField(to='app.jobcategory', verbose_name='Categories')),
                ('languages', models.ManyToManyField(to='app.language', verbose_name='Languages')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.qualification', verbose_name='Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url_pattern', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]