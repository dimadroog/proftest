# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=200, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
            },
        ),
        migrations.CreateModel(
            name='HelpProfChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Форма помощи')),
            ],
            options={
                'verbose_name': 'Помощь в выборе профессии',
                'verbose_name_plural': 'Помощь в выборе профессии',
            },
        ),
        migrations.CreateModel(
            name='HowDidYouKnow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Источник информации')),
            ],
            options={
                'verbose_name': 'Источник информации',
                'verbose_name_plural': 'Источники информации',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Область интересов')),
                ('help_text', models.CharField(max_length=200, null=True, verbose_name='Что именно')),
            ],
            options={
                'verbose_name': 'Область интересов',
                'verbose_name_plural': 'Область интересов',
            },
        ),
        migrations.CreateModel(
            name='Junior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_class', models.CharField(max_length=200)),
                ('dream_prof', models.CharField(max_length=200)),
                ('hobby', models.CharField(max_length=200)),
                ('what_is_university', models.CharField(max_length=500)),
                ('know_university_in_city', models.CharField(max_length=200)),
                ('you_friends_in_ugtu', models.CharField(max_length=200)),
                ('if_you_want_ugtu', models.CharField(max_length=200)),
                ('text_deep_learn_subject', models.CharField(max_length=500, null=True)),
                ('text_hobby', models.CharField(max_length=500, null=True)),
                ('text_how_did_you_know', models.CharField(max_length=500, null=True)),
                ('text_know_university_in_city', models.CharField(max_length=500, null=True)),
                ('text_no_if_you_want_ugtu', models.CharField(max_length=500, null=True)),
                ('text_yes_if_you_want_ugtu', models.CharField(max_length=500, null=True)),
                ('text_talk_about_prof', models.CharField(max_length=500, null=True)),
                ('text_what_is_university', models.CharField(max_length=500, null=True)),
                ('how_did_you_know', models.ManyToManyField(to='tests.HowDidYouKnow')),
            ],
        ),
        migrations.CreateModel(
            name='LearnSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название учебного предмета')),
            ],
            options={
                'verbose_name': 'Учебный предмет',
                'verbose_name_plural': 'Учебные предметы',
            },
        ),
        migrations.CreateModel(
            name='Middle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_class', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('hobby', models.CharField(max_length=200)),
                ('future_prof', models.CharField(max_length=200)),
                ('after_nine_class', models.CharField(max_length=200)),
                ('have_chosen_inst', models.CharField(max_length=200)),
                ('have_chosen_training', models.CharField(max_length=200)),
                ('if_you_want_ugtu', models.CharField(max_length=200)),
                ('if_you_want_ugtu_training', models.CharField(max_length=200, null=True)),
                ('text_deep_learn_subject', models.CharField(max_length=500, null=True)),
                ('text_hobby', models.CharField(max_length=500, null=True)),
                ('text_yes_future_prof', models.CharField(max_length=500, null=True)),
                ('text_addict_future_prof', models.CharField(max_length=500, null=True)),
                ('text_priority_prof', models.CharField(max_length=500, null=True)),
                ('text_talk_about_prof', models.CharField(max_length=500, null=True)),
                ('text_help_prof_choice', models.CharField(max_length=500, null=True)),
                ('text_after_nine_class', models.CharField(max_length=500, null=True)),
                ('text_one_have_chosen_inst', models.CharField(max_length=500, null=True)),
                ('text_many_have_chosen_inst', models.CharField(max_length=500, null=True)),
                ('text_one_have_chosen_training', models.CharField(max_length=500, null=True)),
                ('text_many_have_chosen_training', models.CharField(max_length=500, null=True)),
                ('text_no_if_you_want_ugtu', models.CharField(max_length=500, null=True)),
                ('text_yes_if_you_want_ugtu', models.CharField(max_length=500, null=True)),
                ('text_if_you_want_ugtu_training', models.CharField(max_length=500, null=True)),
                ('deep_learn_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mid_deep_learn_subjects', to='tests.LearnSubjects')),
                ('help_prof_choice', models.ManyToManyField(to='tests.HelpProfChoice')),
                ('learn_subjects', models.ManyToManyField(related_name='mid_learn_subjects', to='tests.LearnSubjects')),
            ],
        ),
        migrations.CreateModel(
            name='PriorityProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Критерий')),
            ],
            options={
                'verbose_name': 'Критерии выбора будующей профессии',
                'verbose_name_plural': 'Критерии выбора будующей профессии',
            },
        ),
        migrations.CreateModel(
            name='RespondentInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, verbose_name='Отношение')),
                ('progress', models.CharField(max_length=500, verbose_name='Достижения')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Interests')),
                ('middle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='tests.Middle')),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='TalkAboutProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Собеседник о профессиях')),
            ],
            options={
                'verbose_name': 'Собеседник о профессиях',
                'verbose_name_plural': 'Собеседники о профессиях',
            },
        ),
        migrations.AddField(
            model_name='middle',
            name='priority_prof',
            field=models.ManyToManyField(to='tests.PriorityProf'),
        ),
        migrations.AddField(
            model_name='middle',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Schools'),
        ),
        migrations.AddField(
            model_name='middle',
            name='talk_about_prof',
            field=models.ManyToManyField(to='tests.TalkAboutProf'),
        ),
        migrations.AddField(
            model_name='junior',
            name='learn_subjects',
            field=models.ManyToManyField(related_name='jun_learn_subjects', to='tests.LearnSubjects'),
        ),
        migrations.AddField(
            model_name='junior',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Schools'),
        ),
        migrations.AddField(
            model_name='junior',
            name='talk_about_prof',
            field=models.ManyToManyField(to='tests.TalkAboutProf'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='middle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Middle'),
        ),
    ]