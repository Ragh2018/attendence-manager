# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-08 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0007_student_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]