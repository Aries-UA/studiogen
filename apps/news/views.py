# -*- coding: utf-8 -*-

from settings import *
from django.template import RequestContext, loader
from django.shortcuts import render
from apps.news.models import News

def news(request):
    data = {
        'news': News.objects.all(),
    }
    return render(request, 'news_news.html', data)

def one_news(request, news_id):
    pass