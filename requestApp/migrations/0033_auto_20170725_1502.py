# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0032_auto_20170725_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Timestamp'),
        ),
    ]
