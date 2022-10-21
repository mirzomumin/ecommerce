from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

from user.utils.email_text import text
from user.models import CustomUser


@shared_task
def send_verification_email(user_id):
	user = CustomUser.objects.get(id=user_id)
	subject = 'Verify your email address'
	url = f"{settings.BACKEND_DOMAIN}api/v1/users/confirm/?confirmation-code={user.confirmation_code}"
	message = f"{text}\
		\n\n\
		Verify your email to activate account by clicking on the link below:\n\
		{url}\n \n\
		{text}"
	user_sender = settings.EMAIL_HOST_USER
	to_user = user.email
	email = EmailMessage(
		subject=subject,
		body=message,
		from_email=user_sender,
		to=(to_user,),
	)
	email.send()