from django.contrib import admin
from .models import Candidate, JobCategory, Language, Qualification, Employer, JobPosting, Location ,CV

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Language)
admin.site.register(Qualification)
admin.site.register(Employer)

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'get_categories', 'qualification', 'location', 'job_type', 'salary_type')
    list_filter = ('job_category', 'qualification', 'location', 'job_type', 'salary_type')
    search_fields = ('job_title', 'job_description')
    
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.job_category.all()])
    
    get_categories.short_description = 'Categories'

admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(JobCategory)
admin.site.register(Location)


    
   

