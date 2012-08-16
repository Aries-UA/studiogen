# -*- coding: utf-8 -*-

from settings import MODELTRANSLATION_DEFAULT_LANGUAGE, LANGUAGES
from django.utils.translation import trans_real

class Lang(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Lang, cls).__new__(cls)
        return cls.instance

    def check(self, lang_code):
        not_found = True
        for l in LANGUAGES:
            if l[0] == lang_code:
                not_found = False
                break
        if not_found:
            lang_code = MODELTRANSLATION_DEFAULT_LANGUAGE
        return lang_code

    def get(self, request):
        lang_code = request.session.get('django_language', MODELTRANSLATION_DEFAULT_LANGUAGE)
        return self.check(lang_code)

    def set(self, lang_code):
        trans_real.deactivate()
        trans_real.activate(lang_code)

    def change(self, request):
        request.session['django_language'] = self.check(request.GET.get('ln', MODELTRANSLATION_DEFAULT_LANGUAGE))
        request.session.save()

lang = Lang()
