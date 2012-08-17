# -*- coding: utf-8 -*-

from django.shortcuts import render

def index(request):
    request.HEAD.setHead('/home/')
    print request.HEAD.content
    data = {
        'html': request.HEAD.content,
    }
    return render(request, 'common_index.html', data)
