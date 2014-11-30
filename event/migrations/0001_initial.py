# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAttachment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('attachment', models.FileField(upload_to='')),
                ('datetime_added', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
