# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0006_auto_20171126_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='conditions',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='receivingreaction',
            name='conditions',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
