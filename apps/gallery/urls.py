# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^gallery/$', 'apps.gallery.views.album'),
)
