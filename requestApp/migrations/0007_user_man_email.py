# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0006_auto_20170712_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='man_email',
            field=models.CharField(default='', max_length=100),
        ),
    ]