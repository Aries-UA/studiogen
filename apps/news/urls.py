# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^news/$', 'apps.news.views.news'),
    (r'^news/(?P<news_id>[0-9]+)$', 'apps.news.views.one_news'),
)
