# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
