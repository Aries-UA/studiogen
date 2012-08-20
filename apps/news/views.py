# -*- coding: utf-8 -*-

from settings import *
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.core.urlresolvers import reverse
from apps.news.models import News

def news(request):
    data = {
        'news': News.objects.all(),
    }
    return render(request, 'news_news.html', data)

def one_news(request, news_id):
    news_id = int(news_id)
    if News.objects.filter(id=news_id).exists():
        data = {
            'one': News.objects.filter(id=news_id)[0],
        }
        return render(request, 'news_one.html', data)
    else:
        return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))