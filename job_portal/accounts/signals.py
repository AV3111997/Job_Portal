from django.db.models.signals import post_delete
from django.dispatch import receiver
from app.models import Candidate, Employer
from .models import User

@receiver(post_delete, sender=Candidate)
def delete_user_on_candidate_delete(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()

@receiver(post_delete, sender=Employer)
def delete_user_on_employer_delete(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()