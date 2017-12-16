# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patrols', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrol',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patrol',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='patrol_membership',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patrol_membership',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
