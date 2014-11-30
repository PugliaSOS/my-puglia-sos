from django.db import models
from django.contrib import admin

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

class Meeting(models.Model):
    event = models.ForeignKey('Event')
    datetime = models.DateTimeField('date and time')
    title = models.CharField(max_length=30)
    description = models.TextField()

class EventAttachment(models.Model):
    event = models.ForeignKey('Event')
    attachment = models.FileField()
    datetime_added = models.DateTimeField(auto_now=True)
