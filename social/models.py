from django.db import models
from django.contrib.auth.models import User


class AssociationStatus(models.Model):
    user = models.ForeignKey(User)
    year = models.CharField(max_length=4)
    status = models.BooleanField(default=False)
