# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-14 04:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 2, 14, 4, 34, 37, 769024, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
