# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0015_auto_20170713_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]