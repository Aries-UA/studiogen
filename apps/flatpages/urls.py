# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('apps.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
