# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-06-28 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20190628_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='URL的别名'),
        ),
    ]
