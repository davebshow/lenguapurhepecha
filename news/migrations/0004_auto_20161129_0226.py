# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsindexpage_body_pua'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsindexpage',
            name='title_pua',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='title_sp',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
