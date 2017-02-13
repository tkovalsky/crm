# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20170213_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='company',
            name='web_site',
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='email_composition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='web_site_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='updateme', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='touch',
            name='follow_up_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]