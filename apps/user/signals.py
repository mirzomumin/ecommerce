from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import CustomUser
from .tasks import send_verification_email

@receiver(post_save, sender=CustomUser)
def send_verification_email_to_user(sender, instance, created, **kwargs):
    if created:
        send_verification_email.delay(instance.id)