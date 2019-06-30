# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=32)),
                ('age', models.CharField(verbose_name='年龄', max_length=32)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=32)),
                ('company', models.CharField(verbose_name='公司', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('money', models.IntegerField(verbose_name='付费金额')),
                ('create_time', models.DateTimeField(verbose_name='付费时间', auto_now_add=True)),
                ('customer', models.ForeignKey(verbose_name='关联客户', to='web.Customer')),
            ],
        ),
    ]
