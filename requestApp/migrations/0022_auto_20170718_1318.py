# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0021_auto_20170718_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='tracker',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]