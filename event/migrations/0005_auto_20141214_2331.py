# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20141214_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattachment',
            name='attachment',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
