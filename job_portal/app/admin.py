from django.contrib import admin
from .models import JobPosting, Category, Qualification, Location

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'category', 'qualification', 'location', 'job_type', 'salary_type')
    list_filter = ('category', 'qualification', 'location', 'job_type', 'salary_type')
    search_fields = ('job_title', 'job_description')

admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Category)
admin.site.register(Qualification)
admin.site.register(Location)
