# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^language/set/$', 'apps.lang.views.set_language'),
)
