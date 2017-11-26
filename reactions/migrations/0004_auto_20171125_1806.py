# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0003_auto_20171125_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='receiving',
        ),
        migrations.AlterField(
            model_name='reaction',
            name='organic_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.OrganicClass'),
        ),
    ]