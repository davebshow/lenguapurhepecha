# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_resourceindexpage_body_pua'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceindexpage',
            name='title_pua',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='resourceindexpage',
            name='title_sp',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]