# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180706_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='_type',
            new_name='order_type',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='_payment',
            new_name='payment_method',
        ),
    ]