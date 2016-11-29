# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='body_en',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_sp',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]