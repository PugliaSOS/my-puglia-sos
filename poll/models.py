from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, null=True)
    html = models.TextField()

    def __str__(self):
        return self.name

class Submitting(models.Model):
    poll = models.ForeignKey('Poll')
    event = models.ForeignKey('event.Event')
    user = models.ForeignKey(User)
    answer = models.TextField()
