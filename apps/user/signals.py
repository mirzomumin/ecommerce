from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from user.utils.email import send_html_mail

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        send_html_mail(instance)