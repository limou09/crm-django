# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=32)),
                ('url', models.CharField(verbose_name='含正则的URL', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='角色名称', max_length=32)),
                ('permissions', models.ManyToManyField(verbose_name='拥有的权限', blank=True, to='rbac.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=32)),
                ('password', models.CharField(verbose_name='密码', max_length=64)),
                ('email', models.CharField(verbose_name='邮箱', max_length=32)),
                ('roles', models.ManyToManyField(verbose_name='拥有的角色', blank=True, to='rbac.Role')),
            ],
        ),
    ]
