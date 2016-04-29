# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20160421_0922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='junior',
            options={'verbose_name': 'Анкета учащегося 5-6-7 классов', 'verbose_name_plural': 'Анкеты учащихся 5-6-7 классов'},
        ),
        migrations.AlterModelOptions(
            name='middle',
            options={'verbose_name': 'Анкета учащегося 8-9 классов', 'verbose_name_plural': 'Анкеты учащихся 8-9 классов'},
        ),
        migrations.AlterModelOptions(
            name='senior',
            options={'verbose_name': 'Анкета учащегося 10-11 классов', 'verbose_name_plural': 'Анкеты учащихся 10-11 классов'},
        ),
        migrations.AlterField(
            model_name='senior',
            name='after_school',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='future_prof',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='have_chosen_inst',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='have_chosen_training',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='if_you_want_ugtu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='senior',
            name='prepare_to_enter',
            field=models.ManyToManyField(null=True, to='tests.PrepareToEnter'),
        ),
        migrations.AlterField(
            model_name='senior',
            name='why_this_inst',
            field=models.ManyToManyField(null=True, to='tests.WhyThisInst'),
        ),
    ]
