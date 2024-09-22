from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('candidate', 'Candidate'),
        ('employer', 'Employer'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=None,
        blank=True,null= True
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return self.email
    
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    gen_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Password reset for {self.user.username}"