# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_verified', models.BinaryField(default=False)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
