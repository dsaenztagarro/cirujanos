# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 21:33
from __future__ import unicode_literals

from django.db import migrations

def insert_location(apps, schema_editor):
    # We can't import the Location model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Location = apps.get_model("about", "Location")
    Location.objects.create(
        name      = "Hospital Quirónsalud Valencia",
        address   = "46010, Avinguda Blasco Ibáñez, 14, 46920 Valencia, Valencia",
        latitude  = "39.478258",
        longitude = "-0.364120")

class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_location'),
    ]

    operations = [
        migrations.RunPython(insert_location),
    ]
