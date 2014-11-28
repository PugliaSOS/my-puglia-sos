from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

class Meeting(models.Model):
    event = models.ForeignKey('Event')
    datetime = models.DateTimeField()
    title = models.CharField(max_length=30)
    description = models.TextFied()

class EventAttachment(models.Model):
    event = models.ForeignKey('Event')
    attachment = models.FileField()
    datetime_added = models.DateTimeField(auto_now=True)
