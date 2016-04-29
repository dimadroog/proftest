# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20160419_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeepLearnSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название учебного предмета углубленного изучения')),
            ],
            options={
                'verbose_name_plural': 'Учебные предметы углубленного изучения',
                'verbose_name': 'Учебный предмет углубленного изучения',
            },
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(blank=True, max_length=200, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='middle',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tests.Middle'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(blank=True, max_length=200, verbose_name='Телефон'),
        ),
        migrations.RemoveField(
            model_name='junior',
            name='deep_learn_subject',
        ),
        migrations.RemoveField(
            model_name='middle',
            name='deep_learn_subject',
        ),
        migrations.AddField(
            model_name='junior',
            name='deep_learn_subject',
            field=models.ManyToManyField(null=True, related_name='jun_deep_learn_subjects', to='tests.DeepLearnSubjects'),
        ),
        migrations.AddField(
            model_name='middle',
            name='deep_learn_subject',
            field=models.ManyToManyField(null=True, related_name='mid_deep_learn_subjects', to='tests.DeepLearnSubjects'),
        ),
    ]