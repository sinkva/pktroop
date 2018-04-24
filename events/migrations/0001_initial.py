# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 04:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrived_date', models.DateField(blank=True, null=True)),
                ('departed_date', models.DateField(blank=True, null=True)),
                ('actual_short_term_camping_nights', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('actual_long_term_camping_nights', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('actual_service_hours', models.FloatField(blank=True, null=True)),
                ('beforehand_contacted_by_PL', models.NullBooleanField()),
                ('not_going_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_scout', models.NullBooleanField()),
                ('lead_asm', models.NullBooleanField()),
                ('two_deep_adult_leader', models.NullBooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_participants',
            field=models.ManyToManyField(through='events.Event_Participation', to=settings.AUTH_USER_MODEL),
        ),
    ]