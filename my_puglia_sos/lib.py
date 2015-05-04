import django.core.mail
import settings.local


def send_mail(user, subject, text):
    text = "Gentile " + user.name + "\n" + text
    mail.send_mail(subject, text, local.EMAIL_HOST, [user.username], fail_silently=False)


