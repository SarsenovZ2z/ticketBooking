# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CountriesAndCities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='country_id',
            new_name='country',
        ),
    ]
