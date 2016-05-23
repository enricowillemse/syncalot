# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SyncAlot', '0004_auto_20160522_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scraper',
            name='id',
        ),
        migrations.AddField(
            model_name='producturl',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='producturl',
            name='name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='host',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
