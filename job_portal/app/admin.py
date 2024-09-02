from django.contrib import admin
from .models import Candidate, JobCategory, Language, Qualification, Employer, JobPosting, Location

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Language)
admin.site.register(Qualification)
admin.site.register(Employer)

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'category', 'qualification', 'location', 'job_type', 'salary_type')
    list_filter = ('category', 'qualification', 'location', 'job_type', 'salary_type')
    search_fields = ('job_title', 'job_description')

admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(JobCategory)
admin.site.register(Location)
