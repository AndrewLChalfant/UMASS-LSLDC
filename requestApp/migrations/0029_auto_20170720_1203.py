# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0028_auto_20170719_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='UCard_ID',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='man_email',
            field=models.EmailField(max_length=50, verbose_name='Manager Email'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='manager',
            field=models.CharField(max_length=50, verbose_name='Manager Name'),
        ),
    ]
