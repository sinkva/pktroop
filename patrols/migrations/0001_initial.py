# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 04:17
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
            name='Patrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patrol_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patrol_Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('patrol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrols.Patrol')),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='patrol',
            name='patrol_members',
            field=models.ManyToManyField(through='patrols.Patrol_Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
