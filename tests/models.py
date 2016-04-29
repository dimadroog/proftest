from django.db import models

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=200, verbose_name='Школа')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.name


class LearnSubjects(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название учебного предмета')

    class Meta:
        verbose_name = 'Учебный предмет'
        verbose_name_plural = 'Учебные предметы'

    def __str__(self):
        return self.name


class DeepLearnSubjects(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название учебного предмета углубленного изучения')

    class Meta:
        verbose_name = 'Учебный предмет углубленного изучения'
        verbose_name_plural = 'Учебные предметы углубленного изучения'

    def __str__(self):
        return self.name


class HowDidYouKnow(models.Model):
    name = models.CharField(max_length=200, verbose_name='Источник информации')

    class Meta:
        verbose_name = 'Источник информации об УГТУ'
        verbose_name_plural = 'Источники информации об УГТУ'

    def __str__(self):
        return self.name


class TalkAboutProf(models.Model):
    name = models.CharField(max_length=200, verbose_name='Собеседник о профессиях')

    class Meta:
        verbose_name = 'Собеседник о профессиях'
        verbose_name_plural = 'Собеседники о профессиях'

    def __str__(self):
        return self.name


class HelpProfChoice(models.Model):
    name = models.CharField(max_length=200, verbose_name='Форма помощи')

    class Meta:
        verbose_name = 'Помощь в выборе профессии'
        verbose_name_plural = 'Помощь в выборе профессии'

    def __str__(self):
        return self.name


class PriorityProf(models.Model):
    name = models.CharField(max_length=200, verbose_name='Критерий')

    class Meta:
        verbose_name = 'Критерии выбора будующей профессии'
        verbose_name_plural = 'Критерии выбора будующей профессии'

    def __str__(self):
        return self.name


class StudentsLife(models.Model):
    name = models.CharField(max_length=200, verbose_name='Сфера')

    class Meta:
        verbose_name = 'Сфера студенческой жизни'
        verbose_name_plural = 'Сферы студенческой жизни'

    def __str__(self):
        return self.name


class WhyThisInst(models.Model):
    name = models.CharField(max_length=200, verbose_name='Критерий')

    class Meta:
        verbose_name = 'Критерии выбора ВУЗа'
        verbose_name_plural = 'Критерии выбора ВУЗа'

    def __str__(self):
        return self.name


class PrepareToEnter(models.Model):
    name = models.CharField(max_length=200, verbose_name='Способ')

    class Meta:
        verbose_name = 'Способ подготовки к поступлению'
        verbose_name_plural = 'Способы подготовки к поступлению'

    def __str__(self):
        return self.name


class Junior(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    view = models.BooleanField(default=False)
    school = models.ForeignKey(Schools)
    learn_subjects = models.ManyToManyField(LearnSubjects, related_name='jun_learn_subjects')
    how_did_you_know = models.ManyToManyField(HowDidYouKnow, related_name='how_did_you_know')
    talk_about_prof = models.ManyToManyField(TalkAboutProf, related_name='jun_talk_about_prof')
    school_class = models.CharField(max_length=200)
    dream_prof = models.CharField(max_length=200)
    deep_learn_subject = models.ManyToManyField(DeepLearnSubjects, related_name='jun_deep_learn_subjects')
    hobby = models.CharField(max_length=200)
    what_is_university = models.CharField(max_length=500)
    know_university_in_city = models.CharField(max_length=200)
    you_friends_in_ugtu = models.CharField(max_length=200)
    if_you_want_ugtu = models.CharField(max_length=200)

    text_hobby = models.CharField(max_length=500, null=True)
    text_how_did_you_know = models.CharField(max_length=500, null=True)
    text_know_university_in_city = models.CharField(max_length=500, null=True)
    text_no_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_yes_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_talk_about_prof = models.CharField(max_length=500, null=True)
    text_what_is_university = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Анкета учащегося 5-6-7 классов'
        verbose_name_plural = 'Анкеты учащихся 5-6-7 классов'

    def __str__(self):
        return str(self.date)


class Middle(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    view = models.BooleanField(default=False)
    school = models.ForeignKey(Schools)
    school_class = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    learn_subjects = models.ManyToManyField(LearnSubjects, related_name='mid_learn_subjects')
    deep_learn_subject = models.ManyToManyField(DeepLearnSubjects, related_name='mid_deep_learn_subjects')
    hobby = models.CharField(max_length=200)
    future_prof = models.CharField(max_length=200)
    priority_prof = models.ManyToManyField(PriorityProf, related_name='mid_priority_prof')
    talk_about_prof = models.ManyToManyField(TalkAboutProf, related_name='mid_talk_about_prof')
    help_prof_choice = models.ManyToManyField(HelpProfChoice, related_name='mid_help_prof_choice')
    after_nine_class = models.CharField(max_length=200)
    have_chosen_inst = models.CharField(max_length=200)
    have_chosen_training = models.CharField(max_length=200)
    if_you_want_ugtu = models.CharField(max_length=200)
    if_you_want_ugtu_training = models.CharField(max_length=200, null=True)

    text_deep_learn_subject = models.CharField(max_length=500, null=True)
    text_hobby = models.CharField(max_length=500, null=True)
    text_yes_future_prof = models.CharField(max_length=500, null=True)
    text_addict_future_prof = models.CharField(max_length=500, null=True)
    text_priority_prof = models.CharField(max_length=500, null=True)
    text_talk_about_prof = models.CharField(max_length=500, null=True)
    text_help_prof_choice = models.CharField(max_length=500, null=True)
    text_after_nine_class = models.CharField(max_length=500, null=True)
    text_one_have_chosen_inst = models.CharField(max_length=500, null=True)
    text_many_have_chosen_inst = models.CharField(max_length=500, null=True)
    text_one_have_chosen_training = models.CharField(max_length=500, null=True)
    text_many_have_chosen_training = models.CharField(max_length=500, null=True)
    text_no_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_yes_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_if_you_want_ugtu_training = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Анкета учащегося 8-9 классов'
        verbose_name_plural = 'Анкеты учащихся 8-9 классов'

    def __str__(self):
        return str(self.date)


class Senior(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    view = models.BooleanField(default=False)
    school = models.ForeignKey(Schools)
    school_class = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    future_prof = models.CharField(max_length=200, null=True)
    help_prof_choice = models.ManyToManyField(HelpProfChoice, related_name='sen_help_prof_choice')
    after_school = models.CharField(max_length=200, null=True)
    have_chosen_inst = models.CharField(max_length=200, null=True)
    why_this_inst = models.ManyToManyField(WhyThisInst, related_name='sen_why_this_inst')
    have_chosen_training = models.CharField(max_length=200, null=True)
    prepare_to_enter = models.ManyToManyField(PrepareToEnter, related_name='sen_prepare_to_enter')
    if_you_want_ugtu = models.CharField(max_length=200, null=True)
    if_you_want_ugtu_training = models.CharField(max_length=200, null=True)
    students_life = models.ManyToManyField(StudentsLife, related_name='sen_students_life')

    text_yes_future_prof = models.CharField(max_length=500, null=True)
    text_addict_future_prof = models.CharField(max_length=500, null=True)
    text_help_prof_choice = models.CharField(max_length=500, null=True)
    text_after_school = models.CharField(max_length=500, null=True)
    text_one_have_chosen_inst = models.CharField(max_length=500, null=True)
    text_many_have_chosen_inst = models.CharField(max_length=500, null=True)
    text_why_this_inst = models.CharField(max_length=500, null=True)
    text_one_have_chosen_training = models.CharField(max_length=500, null=True)
    text_many_have_chosen_training = models.CharField(max_length=500, null=True)
    text_coach_prepare_to_enter = models.CharField(max_length=500, null=True)
    text_course_prepare_to_enter = models.CharField(max_length=500, null=True)
    text_other_prepare_to_enter = models.CharField(max_length=500, null=True)
    text_no_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_yes_if_you_want_ugtu = models.CharField(max_length=500, null=True)
    text_if_you_want_ugtu_training = models.CharField(max_length=500, null=True)
    text_students_life = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'Анкета учащегося 10-11 классов'
        verbose_name_plural = 'Анкеты учащихся 10-11 классов'

    def __str__(self):
        return str(self.date)


class Interests(models.Model):
    name = models.CharField(max_length=200, verbose_name='Область интересов')
    help_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Что именно')

    class Meta:
        verbose_name = 'Область интересов'
        verbose_name_plural = 'Область интересов'

    def __str__(self):
        return self.name


class RespondentInterests(models.Model):
    middle = models.ForeignKey(Middle, null=True, related_name='interests')
    senior = models.ForeignKey(Senior, null=True, related_name='senior_interests')
    interest = models.ForeignKey(Interests, related_name='respondent_interest')
    status = models.CharField(max_length=200, verbose_name='Отношение')
    progress = models.CharField(max_length=500, verbose_name='Достижения')


class Contacts(models.Model):
    middle = models.ForeignKey(Middle, blank=True, null=True, related_name='middle_contacts')
    senior = models.ForeignKey(Senior, blank=True, null=True, related_name='senior_contacts')
    last_name = models.CharField(max_length=200, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, blank=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=200, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=200, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=200, blank=True, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return self.last_name
