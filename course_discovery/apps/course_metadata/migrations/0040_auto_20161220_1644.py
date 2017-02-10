# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-20 16:44
from __future__ import unicode_literals

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0039_programtype_logo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='programtype',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='Leave this field blank to have the value generated automatically.', populate_from='name'),
        ),
        migrations.AlterField(
            model_name='program',
            name='marketing_slug',
            field=models.CharField(db_index=True, help_text='Slug used to generate links to the marketing site', max_length=255, unique=True),
        ),
    ]
