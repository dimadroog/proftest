# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20160419_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='middle',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='middle_contacts', to='tests.Middle'),
        ),
    ]
