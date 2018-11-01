# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-01 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update', models.BooleanField(default=False, verbose_name='更新权限')),
                ('delete', models.BooleanField(default=False, verbose_name='删除权限')),
                ('change', models.BooleanField(default=False, verbose_name='修改权限')),
                ('select', models.BooleanField(default=True, verbose_name='查看权限')),
                ('personnel', models.BooleanField(default=False, verbose_name='人事部权限')),
                ('finance', models.BooleanField(default=False, verbose_name='财务部权限')),
                ('technology', models.BooleanField(default=False, verbose_name='技术部权限')),
                ('sales', models.BooleanField(default=False, verbose_name='销售部权限')),
                ('boss', models.BooleanField(default=False, verbose_name='boss权限')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=32, verbose_name='角色名')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=32, null=True, verbose_name='地址')),
                ('phone_num', models.CharField(max_length=16, null=True, verbose_name='电话')),
                ('image', models.ImageField(default='static/img/default.png', upload_to='static/img', verbose_name='头像')),
                ('gender', models.CharField(max_length=4, verbose_name='性别')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_management.PermissionInfo', verbose_name='权限信息'),
        ),
        migrations.AddField(
            model_name='permission',
            name='role',
            field=models.ManyToManyField(to='user_management.Role', verbose_name='角色'),
        ),
    ]
