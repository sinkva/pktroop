# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180408_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
    ]