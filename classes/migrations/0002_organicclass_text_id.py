# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organicclass',
            name='text_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]