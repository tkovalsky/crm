# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0018_auto_20170213_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='type_of_business',
            field=models.CharField(blank=True, choices=[('elect', 'Electrician'), ('plumb', 'Plumber'), ('hvac', 'HVAC'), ('re', 'Real Estate'), ('uncls', 'Not Classified')], default='uncls', help_text='Business type', max_length=5),
        ),
    ]
