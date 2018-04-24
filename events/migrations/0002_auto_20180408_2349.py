# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='camping_trip',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='full_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='meeting',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='misc_troop_activity',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='outing_non_camping',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='possible_long_term_camping_nights',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='possible_service_hours',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='possible_short_term_camping_nights',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='service_project',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]