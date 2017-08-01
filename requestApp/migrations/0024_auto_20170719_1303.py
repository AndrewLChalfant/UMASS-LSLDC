# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requestApp', '0023_auto_20170719_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='colouser',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='COLOUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='UCard_ID',
            field=models.PositiveIntegerField(blank=True, default='', help_text='HELP'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='man_approved',
            field=models.BooleanField(default='False', verbose_name='Manager Approved'),
        ),
        migrations.AlterField(
            model_name='colouser',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Timestamp'),
        ),
    ]