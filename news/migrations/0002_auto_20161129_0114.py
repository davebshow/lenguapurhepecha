# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsindexpage',
            old_name='body',
            new_name='body_en',
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='body_sp',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
