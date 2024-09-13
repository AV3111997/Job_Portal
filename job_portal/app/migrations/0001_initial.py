# Generated by Django 5.0.8 on 2024-09-13 08:41

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
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_awarded', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
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
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
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
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
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
                ('bio', models.TextField(default='No bio available')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv_files/')),
                ('awards', models.ManyToManyField(blank=True, related_name='candidates', to='app.award')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_profile', to=settings.AUTH_USER_MODEL)),
                ('educations', models.ManyToManyField(blank=True, related_name='candidates', to='app.education')),
                ('job_category', models.ManyToManyField(blank=True, to='app.jobcategory', verbose_name='category')),
                ('languages', models.ManyToManyField(to='app.language', verbose_name='Languages')),
                ('skills', models.ManyToManyField(blank=True, to='app.professionalskill', verbose_name='Professional Skills')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.qualification', verbose_name='Qualification')),
                ('work_experiences', models.ManyToManyField(blank=True, related_name='candidates', to='app.workexperience')),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='cvs/')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_cv', to='app.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('founded_date', models.DateField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='employer_logos/')),
                ('cover_photo', models.ImageField(upload_to='employer_coverphoto/')),
                ('company_size', models.CharField(max_length=20)),
                ('introduction_video_url', models.URLField()),
                ('description', models.CharField(max_length=255)),
                ('profile_url', models.URLField()),
                ('is_open_job', models.BooleanField(default=True)),
                ('saved_candidates', models.ManyToManyField(blank=True, related_name='saved_by_employers', to='app.candidate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to=settings.AUTH_USER_MODEL)),
                ('job_category', models.ManyToManyField(blank=True, to='app.jobcategory', verbose_name='job_category')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('employer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.employer')),
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
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('apply_type', models.CharField(choices=[('online', 'Online'), ('inperson', 'Inperson')], max_length=50)),
                ('urgency_level', models.CharField(choices=[('Urgent', 'Urgent'), ('Normal', 'Normal'), ('Immediate', 'Immediate')], max_length=10)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('apply_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('salary_type', models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Hourly', 'Hourly'), ('Yearly', 'Yearly')], default='Monthly', max_length=50)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('experience', models.CharField(choices=[('0', 'Fresher'), ('1', '1 Year'), ('2', '2 Years'), ('3', '3 Years'), ('4', '4 Years'), ('5', '5 Years'), ('6', '6 Years')], default='Fresher', max_length=50)),
                ('career_level', models.CharField(choices=[('entry', 'Entry-Level'), ('senior', 'Senior-Level')], max_length=50)),
                ('intro_video_url', models.URLField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('filled', 'Filled'), ('draft', 'Draft')], default='open', max_length=50)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('friendly_address', models.CharField(max_length=255)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to='app.employer')),
                ('job_category', models.ManyToManyField(blank=True, to='app.jobcategory', verbose_name='job_category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('reviewed', 'Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=50)),
                ('candidate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobposting')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_contacts', to='app.employer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_contacts', to='app.location')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_contacts', to='app.candidate')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_contacts', to='app.location')),
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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_candidates', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='app.jobposting')),
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
