# -*- coding: utf-8 -*-

from apps.lang.lang import lang
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson

def set_language(request):
    lang.change(request)
    return HttpResponse(simplejson.dumps({'error': 0,}))
