# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-06-28 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_permission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='URL的别名'),
        ),
    ]
