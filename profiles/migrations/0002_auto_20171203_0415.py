# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.CharField(max_length=50)),
                ('street2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='join_troop_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date joined troop'),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Address'),
        ),
    ]
