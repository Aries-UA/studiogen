# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^news/$', 'apps.news.views.news'),
    url(r'^news/(?P<news_id>[0-9]+)/$', 'apps.news.views.one_news', name='one_news'),
)
