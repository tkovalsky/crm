# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20170212_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='update me', max_length=60),
            preserve_default=False,
        ),
    ]
