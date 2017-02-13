# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_note_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contacts',
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Company'),
        ),
    ]