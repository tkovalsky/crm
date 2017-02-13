# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20170131_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'opportunities'},
        ),
        migrations.AlterModelOptions(
            name='touch',
            options={'verbose_name_plural': 'touches'},
        ),
        migrations.AddField(
            model_name='opportunity',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='detail',
            field=models.TextField(),
        ),
    ]