# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('reactions', '0004_auto_20171125_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivingReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('materials', models.CharField(max_length=128)),
                ('products', models.CharField(max_length=128)),
                ('conditions', models.CharField(max_length=128)),
                ('organic_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.OrganicClass')),
            ],
            options={
                'verbose_name': 'Реакция получения',
                'verbose_name_plural': 'Реакции получения',
            },
        ),
    ]
