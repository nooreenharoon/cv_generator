# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='Qualification',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='achievement',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='course',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='job_experience',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='references',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='year',
        ),
    ]
