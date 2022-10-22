from django.core.mail import EmailMessage
from django.conf import settings
from threading import Thread
# from asgiref.sync import sync_to_async

from .email_text import text
from user.models import CustomUser


class EmailThread(Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content,
            settings.EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()


def send_html_mail(user):
	subject = 'Verify your email address'
	url = f"{settings.BACKEND_DOMAIN}api/v1/users/confirm/?confirmation-code={user.confirmation_code}"
	html_content = f'{text}\
		\n\n\
		Verify your email to activate account by clicking on the link below:\n\
		"{url}" \n \n\
		{text}'
	recipient_list = (user.email,)
	EmailThread(subject, html_content, recipient_list).start()