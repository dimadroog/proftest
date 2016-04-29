from django.contrib import admin
from tests.models import Schools, DeepLearnSubjects, LearnSubjects, HowDidYouKnow, TalkAboutProf, Interests, HelpProfChoice, PriorityProf, \
    StudentsLife, WhyThisInst, PrepareToEnter, Junior, Middle, Senior
# Register your models here.
admin.site.register(Schools)
admin.site.register(LearnSubjects)
admin.site.register(DeepLearnSubjects)
# admin.site.register(HowDidYouKnow)
# admin.site.register(TalkAboutProf)
# admin.site.register(Interests)
# admin.site.register(PriorityProf)
# admin.site.register(HelpProfChoice)
# admin.site.register(WhyThisInst)
# admin.site.register(PrepareToEnter)
# admin.site.register(StudentsLife)
admin.site.register(Junior)
admin.site.register(Middle)
admin.site.register(Senior)
