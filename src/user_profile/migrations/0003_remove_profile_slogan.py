# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170205_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slogan',
        ),
    ]
