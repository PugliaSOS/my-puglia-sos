from django.conf import settings
from django.core.mail import send_mail as _send_mail


def send_mail(user, subject, text):
    text = "Gentile " + user.first_name + "\n" + text
    _send_mail(subject, text,
               settings.EMAIL_HOST_USER + '@' + settings.EMAIL_HOST,
               [user.username], fail_silently=False)
