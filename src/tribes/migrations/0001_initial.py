# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 19:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('cover_image', models.FileField(default='/media/posts/iceland.jpg', upload_to='posts')),
                ('description', models.TextField(default='Get notified every time we publish a new tip, a new hack or a deal on Adventure Travel.', max_length=1000)),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
