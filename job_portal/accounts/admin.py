from django.contrib import admin
from .models import CustomUser,PasswordReset

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(PasswordReset) 

