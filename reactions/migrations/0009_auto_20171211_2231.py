# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0008_auto_20171211_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivingreaction',
            name='materials_trans',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='receivingreaction',
            name='products_trans',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]