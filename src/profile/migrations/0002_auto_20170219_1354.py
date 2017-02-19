# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0002_auto_20170219_1354'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='category_subscribe',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='profile',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Categ',
        ),
    ]
