# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0027_auto_20170719_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='UCard_ID',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
