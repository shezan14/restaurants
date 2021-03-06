# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='item_photos/', verbose_name='item_photo', width_field='width_field')),
                ('key', models.CharField(blank=True, default='', max_length=128)),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('ratio', models.CharField(default='1:1', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('ordered_in_restaurant', models.IntegerField(blank=True, default=0)),
                ('ordered_in_home', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodCategory'),
        ),
    ]
