# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0018_auto_20170713_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Employee Name'),
        ),
    ]
