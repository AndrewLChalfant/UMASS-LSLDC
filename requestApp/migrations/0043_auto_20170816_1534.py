# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0042_auto_20170816_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='reason',
            field=models.CharField(choices=[('LSLDC Card Access', 'LSLDC Card Access'), ('COLO Area', 'COLO Area')], default='', max_length=20, verbose_name='Reason for request'),
        ),
    ]
