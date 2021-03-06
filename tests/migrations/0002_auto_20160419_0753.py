# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2016-04-19 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='howdidyouknow',
            options={'verbose_name': 'Источник информации об УГТУ', 'verbose_name_plural': 'Источники информации об УГТУ'},
        ),
        migrations.RemoveField(
            model_name='junior',
            name='text_deep_learn_subject',
        ),
        migrations.AddField(
            model_name='junior',
            name='deep_learn_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jun_deep_learn_subjects', to='tests.LearnSubjects'),
        ),
        migrations.AlterField(
            model_name='interests',
            name='help_text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что именно'),
        ),
    ]
