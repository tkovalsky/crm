# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20170131_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name_plural': 'companies'},
        ),
    ]