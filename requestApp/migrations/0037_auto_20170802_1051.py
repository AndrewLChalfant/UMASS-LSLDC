# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0036_auto_20170802_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='Employee Email'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='man_email',
            field=models.EmailField(max_length=40, verbose_name='Manager Email'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='manager',
            field=models.CharField(max_length=30, verbose_name='Manager Name'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='reason',
            field=models.CharField(max_length=50, verbose_name='Reason for Request'),
        ),
    ]
