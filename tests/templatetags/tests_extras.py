from django import template
from collections import Counter
from tests.models import RespondentInterests

register = template.Library()


@register.filter(name='percent')
def percent(value, total):
    if value == '':
        value = 0
    return round(int(value) * 100 / int(total))


@register.simple_tag(name='count_others')
def count_others(objects, field):
    dct = {field: ''}
    result = objects.filter(**dct)
    result = result.count()
    return result


@register.simple_tag(name='summary_interest_status')
def summary_interest_status(interest, group):
    dct = {group: None}
    group_interests = RespondentInterests.objects.exclude(**dct)
    result = group_interests.filter(interest=interest)
    true_result = result.filter(status=1).count()
    false_result = result.filter(status=0).count()
    dictionary = {'tr': true_result, 'fl': false_result}
    return dictionary


@register.simple_tag(name='sum_same_items')
def sum_same_items(objects, field):
    string = ''
    for obj in objects:
        item = getattr(obj, field) + ','
        string += item
    string = string.replace(' ', '')
    string = string.replace(',,', ',nothing,')
    lst = string.split(',')
    dct = dict(Counter(lst[:-1]))

    return dct


@register.simple_tag(name='count_by_str')
def count_by_str(objects, field, string):
    dictionary = {}
    for lst in string.split():
        dictionary[lst] = 0
    for obj in objects:
        item = getattr(obj, field)
        if item in dictionary:
            dictionary[item] += 1
    return dictionary

