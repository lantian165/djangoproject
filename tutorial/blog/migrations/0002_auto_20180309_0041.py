# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 16:41
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u6587\u7ae0\u6b63\u6587'),
        ),
    ]
