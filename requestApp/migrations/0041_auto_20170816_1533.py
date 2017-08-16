# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0040_auto_20170816_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='dep',
            field=models.CharField(choices=[('UMass Amherst', 'UMass Amherst'), ('UMass Boston', 'UMass Boston'), ("UMass President's Office", " UMass President's Office"), ('UMass Medical School', 'UMass Medical School')], default='', max_length=20, verbose_name='Campus'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='reason',
            field=models.CharField(choices=[('UMass Amherst', 'UMass Amherst'), ('UMass Boston', 'UMass Boston'), ("UMass President's Office", " UMass President's Office"), ('UMass Medical School', 'UMass Medical School')], default='', max_length=20, verbose_name='Campus'),
        ),
    ]
