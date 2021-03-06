# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20170127_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('date', models.DateField()),
                ('touch_type', models.CharField(max_length=20)),
                ('detail', models.TextField()),
                ('follow_up_date', models.CharField(max_length=20)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='business',
            name='contact',
            field=models.ManyToManyField(blank=True, to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='note',
            name='contact',
            field=models.ManyToManyField(to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='touch',
            name='contact',
            field=models.ManyToManyField(to='contacts.Contact'),
        ),
    ]
