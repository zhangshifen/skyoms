# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_ip', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='\u5185\u7f51IP')),
                ('ex_ip', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u5916\u7f51IP')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('host_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4f4d\u7f6e')),
                ('cpu_model', models.CharField(blank=True, max_length=255, null=True, verbose_name='CPU\u578b\u53f7')),
                ('cpu_cores', models.IntegerField(blank=True, null=True, verbose_name='CPU\u6838\u6570')),
                ('cpu_count', models.IntegerField(blank=True, null=True, verbose_name='CPU\u4e2a\u6570')),
                ('mem', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u5185\u5b58')),
                ('disk', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u78c1\u76d8')),
                ('os_version', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('os_kernel', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7cfb\u7edf\u5185\u6838')),
                ('status', models.NullBooleanField(default=False, verbose_name='\u8fd0\u884c\u72b6\u6001')),
                ('max_open_files', models.IntegerField(blank=True, null=True, verbose_name='\u6700\u5927\u6253\u5f00\u6587\u4ef6\u6570')),
                ('uptime', models.IntegerField(blank=True, null=True, verbose_name='\u5728\u7ebf\u65f6\u95f4\uff08\u5929\uff09')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7aef\u53e3')),
                ('service_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u670d\u52a1\u540d')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server', verbose_name='\u670d\u52a1\u5668')),
            ],
        ),
    ]
