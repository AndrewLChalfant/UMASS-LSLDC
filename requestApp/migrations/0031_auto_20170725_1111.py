# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0030_auto_20170720_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='time',
            field=models.DateTimeField(verbose_name='Timestamp'),
        ),
    ]
