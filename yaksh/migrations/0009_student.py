# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-25 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0008_release_0_7_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=255)),
                ('user_last_name', models.CharField(max_length=255)),
            ],
        ),
    ]