from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, null=True)
    poll = models.ForeignKey('poll.Poll', null=True, blank=True)

    def __str__(self):
        return self.title

class Meeting(models.Model):
    event = models.ForeignKey('Event')
    datetime = models.DateTimeField('date and time')
    title = models.CharField(max_length=30)
    description = models.TextField()

class EventAttachment(models.Model):
    event = models.ForeignKey('Event')
    attachment = models.FileField()
    datetime_added = models.DateTimeField(auto_now=True)
