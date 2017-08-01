# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestApp', '0033_auto_20170725_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colouser',
            name='dep',
            field=models.CharField(choices=[('UMass Student', 'UMass Student'), ("President's Office", "President's Office"), ('Medical School', 'Medical School'), ('Other', 'Other')], default='', max_length=20, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='Employee Email'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='man_email',
            field=models.EmailField(max_length=20, verbose_name='Manager Email'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='manager',
            field=models.CharField(max_length=20, verbose_name='Manager Name'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='reason',
            field=models.CharField(max_length=20, verbose_name='Reason for Request'),
        ),
    ]