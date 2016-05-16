from collections import Counter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tests.models import Schools, LearnSubjects, Junior, HowDidYouKnow, TalkAboutProf, PriorityProf, HelpProfChoice, \
    Interests, Middle, RespondentInterests, Contacts, DeepLearnSubjects, WhyThisInst, PrepareToEnter, StudentsLife, \
    Senior
import json


@login_required(login_url='/admin/login/')
def summary(request, group):
    respondents = None
    school_resp = None
    learn_subjects_resp = None
    deep_learn_subjects_resp = None
    how_did_you_know_resp = None
    talk_about_prof_resp = None
    priority_prof_resp = None
    help_prof_choice_resp = None
    interests_resp = None
    why_this_inst_resp = None
    prepare_to_enter_resp = None
    students_life_resp = None
    contacts = None
    header_class = None
    header_school = None
    schools = Schools.objects.all()

    if group == 'junior':
        header_class = '5-6-7'
        header_school = 'Все учебные заведения'

        if request.GET:

            if request.GET.get('school') and not request.GET.get('class'):
                schools = Schools.objects.filter(id=request.GET.get('school'))
                respondents = Junior.objects.filter(school=schools)
                header_school = Schools.objects.get(id=request.GET.get('school')).name

            if request.GET.get('class') and not request.GET.get('school'):
                respondents = Junior.objects.filter(school_class=request.GET.get('class'))
                schools = schools.filter(junior__in=respondents)
                header_class = request.GET.get('class')

            if request.GET.get('class') and request.GET.get('school'):
                respondents = Junior.objects.filter(school=request.GET.get('school'), school_class=request.GET.get('class'))
                schools = Schools.objects.filter(id=request.GET.get('school'))
                header_school = Schools.objects.get(id=request.GET.get('school')).name
                header_class = request.GET.get('class')

        else:
            respondents = Junior.objects.all()

        school_resp = get_items_with_cnt(respondents, schools, 'school')

        learn_subjects = LearnSubjects.objects.all()
        learn_subjects_resp = get_items_with_cnt(respondents, learn_subjects, 'learn_subjects')

        deep_learn_subjects = DeepLearnSubjects.objects.all()
        deep_learn_subjects_resp = get_items_with_cnt(respondents, deep_learn_subjects, 'deep_learn_subject')

        how_did_you_know = HowDidYouKnow.objects.all()
        how_did_you_know_resp = get_items_with_cnt(respondents, how_did_you_know, 'how_did_you_know')

        talk_about_prof = TalkAboutProf.objects.all()
        talk_about_prof_resp = get_items_with_cnt(respondents, talk_about_prof, 'talk_about_prof')

    if group == 'middle':
        header_class = '8-9'
        header_school = 'Все учебные заведения'

        if request.GET:

            if request.GET.get('school') and not request.GET.get('class'):
                schools = Schools.objects.filter(id=request.GET.get('school'))
                respondents = Middle.objects.filter(school=schools)
                header_school = Schools.objects.get(id=request.GET.get('school')).name

            if request.GET.get('class') and not request.GET.get('school'):
                respondents = Middle.objects.filter(school_class=request.GET.get('class'))
                schools = schools.filter(middle__in=respondents)
                header_class = request.GET.get('class')

            if request.GET.get('class') and request.GET.get('school'):
                respondents = Middle.objects.filter(school=request.GET.get('school'), school_class=request.GET.get('class'))
                schools = Schools.objects.filter(id=request.GET.get('school'))
                header_school = Schools.objects.get(id=request.GET.get('school')).name
                header_class = request.GET.get('class')

        else:
            respondents = Middle.objects.all()

        school_resp = get_items_with_cnt(respondents, schools, 'school')

        learn_subjects = LearnSubjects.objects.all()
        learn_subjects_resp = get_items_with_cnt(respondents, learn_subjects, 'learn_subjects')

        deep_learn_subjects = DeepLearnSubjects.objects.all()
        deep_learn_subjects_resp = get_items_with_cnt(respondents, deep_learn_subjects, 'deep_learn_subject')

        talk_about_prof = TalkAboutProf.objects.all()
        talk_about_prof_resp = get_items_with_cnt(respondents, talk_about_prof, 'talk_about_prof')

        priority_prof = PriorityProf.objects.all()
        priority_prof_resp = get_items_with_cnt(respondents, priority_prof, 'priority_prof')

        help_prof_choice = HelpProfChoice.objects.all()
        help_prof_choice_resp = get_items_with_cnt(respondents, help_prof_choice, 'help_prof_choice')

        interests = Interests.objects.all()
        interests_resp = []
        for interest in interests:
            middle_interests = RespondentInterests.objects.exclude(middle=None)
            middle_interests = middle_interests.filter(middle__in=respondents)
            tr = middle_interests.filter(interest=interest, status=1).count()
            fl = middle_interests.filter(interest=interest, status=0).count()
            interests_resp.append({'name': interest.name, 'tr': tr, 'fl': fl})

        contacts = Contacts.objects.exclude(middle__isnull=True)

    if group == 'senior':
        header_class = '10-11'
        header_school = 'Все учебные заведения'

        if request.GET:

            if request.GET.get('school') and not request.GET.get('class'):
                schools = Schools.objects.filter(id=request.GET.get('school'))
                respondents = Senior.objects.filter(school=schools)
                header_school = Schools.objects.get(id=request.GET.get('school')).name

            if request.GET.get('class') and not request.GET.get('school'):
                respondents = Senior.objects.filter(school_class=request.GET.get('class'))
                schools = schools.filter(senior__in=respondents)
                header_class = request.GET.get('class')

            if request.GET.get('class') and request.GET.get('school'):
                respondents = Senior.objects.filter(school=request.GET.get('school'), school_class=request.GET.get('class'))
                schools = Schools.objects.filter(id=request.GET.get('school'))
                header_school = Schools.objects.get(id=request.GET.get('school')).name
                header_class = request.GET.get('class')

        else:
            respondents = Senior.objects.all()

        school_resp = get_items_with_cnt(respondents, schools, 'school')

        help_prof_choice = HelpProfChoice.objects.all()
        help_prof_choice_resp = get_items_with_cnt(respondents, help_prof_choice, 'help_prof_choice')

        why_this_inst = WhyThisInst.objects.all()
        why_this_inst_resp = get_items_with_cnt(respondents, why_this_inst, 'why_this_inst')

        prepare_to_enter = PrepareToEnter.objects.all()
        prepare_to_enter_resp = get_items_with_cnt(respondents, prepare_to_enter, 'prepare_to_enter')

        students_life = StudentsLife.objects.all()
        students_life_resp = get_items_with_cnt(respondents, students_life, 'students_life')

        interests = Interests.objects.all()
        interests_resp = []
        for interest in interests:
            senior_interests = RespondentInterests.objects.exclude(senior=None)
            senior_interests = senior_interests.filter(senior__in=respondents)
            tr = senior_interests.filter(interest=interest, status=1).count()
            fl = senior_interests.filter(interest=interest, status=0).count()
            interests_resp.append({'name': interest.name, 'tr': tr, 'fl': fl})

        contacts = Contacts.objects.exclude(senior__isnull=True)

    return render(request, 'tests/summary.html', {'results': respondents,
                                                  'group': group,
                                                  'header_class': header_class,
                                                  'header_school': header_school,
                                                  'school_resp': school_resp,
                                                  'learn_subjects_resp': learn_subjects_resp,
                                                  'deep_learn_subjects_resp': deep_learn_subjects_resp,
                                                  'how_did_you_know_resp': how_did_you_know_resp,
                                                  'talk_about_prof_resp': talk_about_prof_resp,
                                                  'priority_prof_resp': priority_prof_resp,
                                                  'help_prof_choice_resp': help_prof_choice_resp,
                                                  'interests_resp': interests_resp,
                                                  'contacts': contacts,
                                                  'why_this_inst_resp': why_this_inst_resp,
                                                  'prepare_to_enter_resp': prepare_to_enter_resp,
                                                  'students_life_resp': students_life_resp,
                                                  })


def get_items_with_cnt(respondents, objects, field):
        dct = {}
        for obj in objects:
            cnt = respondents.filter(**{field: obj}).count()
            dct.update({obj: cnt})
        return dct


@login_required(login_url='/admin/login/')
def result(request, group):
    if group == 'junior':
        respondents = Junior.objects.all().order_by('-id')
    if group == 'middle':
        respondents = Middle.objects.all().order_by('-id')
    if group == 'senior':
        respondents = Senior.objects.all().order_by('-id')
    paginator = Paginator(respondents, 10)
    page = request.GET.get('page')
    try:
        resp = paginator.page(page)
    except PageNotAnInteger:
        resp = paginator.page(1)
    except EmptyPage:
        resp = paginator.page(paginator.num_pages)
    return render(request, 'tests/results.html', {'results': resp, 'group': group, })


def junior_test(request):
    schools = Schools.objects.all()
    info_sources = HowDidYouKnow.objects.all()
    talkers_prof = TalkAboutProf.objects.all()
    learn_subjects = LearnSubjects.objects.all()
    deep_learn_subjects = DeepLearnSubjects.objects.all()
    if request.POST:
        save_junior = Junior(
            school=Schools.objects.get(id=request.POST.get('school')),
            school_class=request.POST.get('school_class'),
            dream_prof=request.POST.get('dream_prof'),
            hobby=request.POST.get('hobby'),
            what_is_university=request.POST.get('what_is_university'),
            know_university_in_city=request.POST.get('know_university_in_city'),
            you_friends_in_ugtu=request.POST.get('you_friends_in_ugtu'),
            if_you_want_ugtu=request.POST.get('if_you_want_ugtu'),

            text_hobby=request.POST.get('text_hobby'),
            text_how_did_you_know=request.POST.get('text_how_did_you_know'),
            text_know_university_in_city=request.POST.get('text_know_university_in_city'),
            text_no_if_you_want_ugtu=request.POST.get('text_no_if_you_want_ugtu'),
            text_yes_if_you_want_ugtu=request.POST.get('text_yes_if_you_want_ugtu'),
            text_talk_about_prof=request.POST.get('text_talk_about_prof'),
            text_what_is_university=request.POST.get('text_what_is_university'),
        )
        save_junior.save()
        if request.POST.get('deep_learn_subject'):
            for subj in request.POST.getlist('deep_learn_subject'):
                save_junior.deep_learn_subject.add(subj)
        if request.POST.get('like_learn_subject'):
            for subj in request.POST.getlist('like_learn_subject'):
                save_junior.learn_subjects.add(subj)
        if request.POST.get('how_did_you_know'):
            for subj in request.POST.getlist('how_did_you_know'):
                save_junior.how_did_you_know.add(subj)
        if request.POST.get('talk_about_prof'):
            for subj in request.POST.getlist('talk_about_prof'):
                save_junior.talk_about_prof.add(subj)
        return HttpResponseRedirect('/thanks/')
    return render(request, 'tests/test_junior.html', {'schools': schools,
                                                      'talkers_prof': talkers_prof,
                                                      'info_sources': info_sources,
                                                      'learn_subjects': learn_subjects,
                                                      'deep_learn_subjects': deep_learn_subjects,
                                                      })


def middle_test(request):
    priority_prof = PriorityProf.objects.all()
    schools = Schools.objects.all()
    learn_subjects = LearnSubjects.objects.all()
    talkers_prof = TalkAboutProf.objects.all()
    help_prof_choice = HelpProfChoice.objects.all()
    interests = Interests.objects.all()
    deep_learn_subjects = DeepLearnSubjects.objects.all()
    if request.POST:
        save_middle = Middle(
            school=Schools.objects.get(id=request.POST.get('school')),
            school_class=request.POST.get('school_class'),
            gender=request.POST.get('gender'),
            hobby=request.POST.get('hobby'),
            future_prof=request.POST.get('future_prof'),
            after_nine_class=request.POST.get('after_nine_class'),
            have_chosen_inst=request.POST.get('have_chosen_inst'),
            have_chosen_training=request.POST.get('have_chosen_training'),
            if_you_want_ugtu=request.POST.get('if_you_want_ugtu'),
            if_you_want_ugtu_training=request.POST.get('if_you_want_ugtu_training'),

            text_hobby=request.POST.get('text_hobby'),
            text_addict_future_prof=request.POST.get('text_addict_future_prof'),
            text_yes_future_prof=request.POST.get('text_yes_future_prof'),
            text_priority_prof=request.POST.get('text_priority_prof'),
            text_talk_about_prof=request.POST.get('text_talk_about_prof'),
            text_help_prof_choice=request.POST.get('text_help_prof_choice'),
            text_after_nine_class=request.POST.get('text_after_nine_class'),
            text_one_have_chosen_inst=request.POST.get('text_one_have_chosen_inst'),
            text_many_have_chosen_inst=request.POST.get('text_many_have_chosen_inst'),
            text_one_have_chosen_training=request.POST.get('text_one_have_chosen_training'),
            text_many_have_chosen_training=request.POST.get('text_many_have_chosen_training'),
            text_no_if_you_want_ugtu=request.POST.get('text_no_if_you_want_ugtu'),
            text_yes_if_you_want_ugtu=request.POST.get('text_yes_if_you_want_ugtu'),
            text_if_you_want_ugtu_training=request.POST.get('text_if_you_want_ugtu_training'),
        )
        save_middle.save()
        if request.POST.get('like_learn_subject'):
            for subj in request.POST.getlist('like_learn_subject'):
                save_middle.learn_subjects.add(subj)
        if request.POST.get('deep_learn_subject'):
            for subj in request.POST.getlist('deep_learn_subject'):
                save_middle.deep_learn_subject.add(subj)
        if request.POST.get('priority_prof'):
            for subj in request.POST.getlist('priority_prof'):
                save_middle.priority_prof.add(subj)
        if request.POST.get('talk_about_prof'):
            for subj in request.POST.getlist('talk_about_prof'):
                save_middle.talk_about_prof.add(subj)
        if request.POST.get('help_prof_choice'):
            for subj in request.POST.getlist('help_prof_choice'):
                save_middle.help_prof_choice.add(subj)
        for subj in json.loads(request.POST.get('build_interests')):
            save_respondent_interests = RespondentInterests(
                middle=save_middle,
                interest=Interests.objects.get(id=subj['id']),
                status=subj['status'],
                progress=subj['value'],
            )
            save_respondent_interests.save()
        if request.POST.get('subscribe_last_name') or request.POST.get('subscribe_first_name') or request.POST.get('subscribe_middle_name') or request.POST.get('subscribe_phone') or request.POST.get('subscribe_email'):
            save_contacts = Contacts(
                middle=save_middle,
                last_name=request.POST.get('subscribe_last_name', None),
                first_name=request.POST.get('subscribe_first_name', None),
                middle_name=request.POST.get('subscribe_middle_name', None),
                phone=request.POST.get('subscribe_phone', None),
                email=request.POST.get('subscribe_email', None),
            )
            save_contacts.save()
        return HttpResponseRedirect('/thanks/')

    return render(request, 'tests/test_middle.html', {'priority_prof': priority_prof,
                                                      'schools': schools,
                                                      'learn_subjects': learn_subjects,
                                                      'talkers_prof': talkers_prof,
                                                      'help_prof_choices': help_prof_choice,
                                                      'interests': interests,
                                                      'deep_learn_subjects': deep_learn_subjects,
                                                      })


def senior_test(request):
    schools = Schools.objects.all()
    help_prof_choice = HelpProfChoice.objects.all()
    why_this_inst = WhyThisInst.objects.all()
    prepare_to_enter = PrepareToEnter.objects.all()
    students_life = StudentsLife.objects.all()
    interests = Interests.objects.all()

    if request.POST:
        save_senior = Senior(
            school=Schools.objects.get(id=request.POST.get('school')),
            school_class=request.POST.get('school_class', None),
            gender=request.POST.get('gender', None),
            future_prof=request.POST.get('future_prof', None),
            after_school=request.POST.get('after_school', None),
            have_chosen_inst=request.POST.get('have_chosen_inst', None),
            have_chosen_training=request.POST.get('have_chosen_training', None),
            if_you_want_ugtu=request.POST.get('if_you_want_ugtu', None),
            if_you_want_ugtu_training=request.POST.get('if_you_want_ugtu_training', None),

            text_addict_future_prof=request.POST.get('text_addict_future_prof', None),
            text_yes_future_prof=request.POST.get('text_yes_future_prof', None),
            text_help_prof_choice=request.POST.get('text_help_prof_choice', None),
            text_after_school=request.POST.get('text_after_school', None),
            text_one_have_chosen_inst=request.POST.get('text_one_have_chosen_inst', None),
            text_many_have_chosen_inst=request.POST.get('text_many_have_chosen_inst', None),
            text_why_this_inst=request.POST.get('text_why_this_inst', None),
            text_one_have_chosen_training=request.POST.get('text_one_have_chosen_training', None),
            text_many_have_chosen_training=request.POST.get('text_many_have_chosen_training', None),
            text_coach_prepare_to_enter=request.POST.get('text_coach_prepare_to_enter', None),
            text_course_prepare_to_enter=request.POST.get('text_course_prepare_to_enter', None),
            text_other_prepare_to_enter=request.POST.get('text_other_prepare_to_enter', None),
            text_no_if_you_want_ugtu=request.POST.get('text_no_if_you_want_ugtu', None),
            text_yes_if_you_want_ugtu=request.POST.get('text_yes_if_you_want_ugtu', None),
            text_if_you_want_ugtu_training=request.POST.get('text_if_you_want_ugtu_training', None),
            text_students_life=request.POST.get('text_students_life', None),
        )

        save_senior.save()

        if request.POST.get('help_prof_choice'):
            for subj in request.POST.getlist('help_prof_choice'):
                save_senior.help_prof_choice.add(subj)
        if request.POST.get('why_this_inst'):
            for subj in request.POST.getlist('why_this_inst'):
                save_senior.why_this_inst.add(subj)
        if request.POST.get('prepare_to_enter'):
            for subj in request.POST.getlist('prepare_to_enter'):
                save_senior.prepare_to_enter.add(subj)
        if request.POST.get('students_life'):
            for subj in request.POST.getlist('students_life'):
                save_senior.students_life.add(subj)

        for subj in json.loads(request.POST.get('build_interests')):
            save_respondent_interests = RespondentInterests(
                senior=save_senior,
                interest=Interests.objects.get(id=subj['id']),
                status=subj['status'],
                progress=subj['value'],
            )
            save_respondent_interests.save()
        if request.POST.get('subscribe_last_name') or request.POST.get('subscribe_first_name') or request.POST.get('subscribe_middle_name') or request.POST.get('subscribe_phone') or request.POST.get('subscribe_email'):
            save_contacts = Contacts(
                senior=save_senior,
                last_name=request.POST.get('subscribe_last_name', None),
                first_name=request.POST.get('subscribe_first_name', None),
                middle_name=request.POST.get('subscribe_middle_name', None),
                phone=request.POST.get('subscribe_phone', None),
                email=request.POST.get('subscribe_email', None),
            )
            save_contacts.save()
        return HttpResponseRedirect('/thanks/')
    return render(request, 'tests/test_senior.html', {'schools': schools,
                                                      'help_prof_choices': help_prof_choice,
                                                      'why_this_inst': why_this_inst,
                                                      'prepare_to_enter': prepare_to_enter,
                                                      'students_life': students_life,
                                                      'interests': interests,
                                                      })


@csrf_exempt
def change_view(request):
    if request.POST:
        if request.POST.get('group') == 'junior':
            respondent = Junior.objects.get(id=request.POST.get('id'))
        elif request.POST.get('group') == 'middle':
            respondent = Middle.objects.get(id=request.POST.get('id'))
        elif request.POST.get('group') == 'senior':
            respondent = Senior.objects.get(id=request.POST.get('id'))

        if respondent.view:
            respondent.view = False
            data = 0
        else:
            respondent.view = True
            data = 1
        respondent.save()
        return HttpResponse(data)


@csrf_exempt
def view_other_answers(request):
    if request.POST:
        nothing = ''
        if request.POST.get('group') == 'junior':
            respondents = Junior.objects.all()
            if request.POST.get('school') and not request.POST.get('class'):
                schools = Schools.objects.filter(id=request.POST.get('school'))
                respondents = Junior.objects.filter(school=schools)

            if request.POST.get('class') and not request.POST.get('school'):
                respondents = Junior.objects.filter(school_class=request.POST.get('class'))

            if request.POST.get('class') and request.POST.get('school'):
                respondents = Junior.objects.filter(school=request.POST.get('school'), school_class=request.POST.get('class'))

        if request.POST.get('group') == 'middle':
            respondents = Middle.objects.all()
            if request.POST.get('school') and not request.POST.get('class'):
                schools = Schools.objects.filter(id=request.POST.get('school'))
                respondents = Middle.objects.filter(school=schools)

            if request.POST.get('class') and not request.POST.get('school'):
                respondents = Middle.objects.filter(school_class=request.POST.get('class'))

            if request.POST.get('class') and request.POST.get('school'):
                respondents = Middle.objects.filter(school=request.POST.get('school'), school_class=request.POST.get('class'))

        if request.POST.get('group') == 'senior':
            respondents = Senior.objects.all()
            if request.POST.get('school') and not request.POST.get('class'):
                schools = Schools.objects.filter(id=request.POST.get('school'))
                respondents = Senior.objects.filter(school=schools)

            if request.POST.get('class') and not request.POST.get('school'):
                respondents = Senior.objects.filter(school_class=request.POST.get('class'))

            if request.POST.get('class') and request.POST.get('school'):
                respondents = Senior.objects.filter(school=request.POST.get('school'), school_class=request.POST.get('class'))

        dct = sum_same_items(respondents, request.POST.get('field'))

        lst = []
        for name, cnt in dct.items():
                item = '%s - <b class="text-success">%s</b>;' % (str(name), str(cnt))
                if item:
                    lst.append(item + '<br>')
        if not lst:
            lst = '<span class="text-muted">Ничего нет</span>'
        return HttpResponse(lst)


def sum_same_items(objects, field):
    string = ''
    for obj in objects:
        item = getattr(obj, field)
        if item:
            item = item.strip().lower()
            string += item + ','
    lst = string.split(',')
    dct = dict(Counter(lst[:-1]))
    return dct


@csrf_exempt
def query(request):
    schools = Schools.objects.all()

    if request.GET:
        url = ''
        params = ''

        if request.GET.get('class'):
            if request.GET.get('class') == '5' or request.GET.get('class') == '6' or request.GET.get('class') == '7':
                url = '/summary/junior/'
                params = 'class=%s' % request.GET.get('class')
            if request.GET.get('class') == '8' or request.GET.get('class') == '9':
                url = '/summary/middle/'
                params = 'class=%s' % request.GET.get('class')
            if request.GET.get('class') == '10' or request.GET.get('class') == '11':
                url = '/summary/senior/'
                params = 'class=%s' % request.GET.get('class')

        if request.GET.get('school'):
            params += '&school=%s' % request.GET.get('school')

        return HttpResponseRedirect(url + '?%s' % params)

    return render(request, 'tests/query.html', {'schools': schools})

