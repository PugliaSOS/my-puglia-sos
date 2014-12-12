# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
        ('event', '0002_auto_20141130_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poll',
            field=models.ForeignKey(to='poll.Poll', null=True, blank=True),
            preserve_default=True,
        ),
    ]
