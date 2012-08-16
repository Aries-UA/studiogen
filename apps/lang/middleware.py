# -*- coding: utf-8 -*-

from apps.lang.lang import lang

class LangMiddleware(object):

    def process_request(self, request):
        lang.set(lang.get(request))
