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
    learn_subjects = None
    deep_learn_subjects = None
    how_did_you_know = None
    talk_about_prof = None
    priority_prof = None
    help_prof_choice = None
    interests = None
    contacts = None
    why_this_inst = None
    prepare_to_enter = None
    students_life = None
    if request.GET.get('school'):
        schools = Schools.objects.get(id=request.GET.get('school'))
    else:
        schools = Schools.objects.all()

    if group == 'junior':
        if request.GET.get('school'):
            respondents = Junior.objects.filter(school=schools)
        else:
            respondents = Junior.objects.all()
        learn_subjects = LearnSubjects.objects.all()
        deep_learn_subjects = DeepLearnSubjects.objects.all()
        how_did_you_know = HowDidYouKnow.objects.all()
        talk_about_prof = TalkAboutProf.objects.all()

    if group == 'middle':
        if request.GET.get('school'):
            respondents = Middle.objects.filter(school=schools)
        else:
            respondents = Middle.objects.all()
        learn_subjects = LearnSubjects.objects.all()
        deep_learn_subjects = DeepLearnSubjects.objects.all()
        talk_about_prof = TalkAboutProf.objects.all()
        priority_prof = PriorityProf.objects.all()
        help_prof_choice = HelpProfChoice.objects.all()
        interests = Interests.objects.all()
        contacts = Contacts.objects.exclude(middle__isnull=True)

    if group == 'senior':
        if request.GET.get('school'):
            respondents = Senior.objects.filter(school=schools)
        else:
            respondents = Senior.objects.all()
        help_prof_choice = HelpProfChoice.objects.all()
        why_this_inst = WhyThisInst.objects.all()
        prepare_to_enter = PrepareToEnter.objects.all()
        students_life = StudentsLife.objects.all()
        interests = Interests.objects.all()
        contacts = Contacts.objects.exclude(senior__isnull=True)

    return render(request, 'tests/summary.html', {'results': respondents,
                                                  'group': group,
                                                  'schools': schools,
                                                  'learn_subjects': learn_subjects,
                                                  'deep_learn_subjects': deep_learn_subjects,
                                                  'how_did_you_know': how_did_you_know,
                                                  'talk_about_prof': talk_about_prof,
                                                  'priority_prof': priority_prof,
                                                  'help_prof_choice': help_prof_choice,
                                                  'interests': interests,
                                                  'contacts': contacts,
                                                  'why_this_inst': why_this_inst,
                                                  'prepare_to_enter': prepare_to_enter,
                                                  'students_life': students_life,
                                                  })


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
        if request.POST.get('group') == 'junior':
            respondents = Junior.objects.all()
        elif request.POST.get('group') == 'middle':
            respondents = Middle.objects.all()
        elif request.POST.get('group') == 'senior':
            respondents = Senior.objects.all()

        lst = []
        for respondent in respondents:
            item = getattr(respondent, request.POST.get('field'))
            if item:
                lst.append(item + '<br>')

        if not lst:
            lst = '<span class="text-muted">Ничего нет</span>'
        return HttpResponse(lst)
