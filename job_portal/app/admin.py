from django.contrib import admin
from . models import Candidate, JobCategories, Language, Qualification

# Register your models here.

admin.site.register(Candidate)
admin.site.register(JobCategories)
admin.site.register(Language)
admin.site.register(Qualification)


