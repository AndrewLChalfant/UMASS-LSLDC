# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0003_auto_20170712_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='A', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='A', max_length=100),
        ),
    ]
