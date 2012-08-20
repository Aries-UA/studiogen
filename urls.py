# -*- coding: utf-8 -*-

import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url('', include('apps.common.urls')),
    url('', include('apps.account.urls')),
    url('', include('apps.gallery.urls')),
    url('', include('apps.news.urls')),
    url('', include('apps.contactus.urls')),
    url('', include('apps.lang.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico')),
    (r'^admin/', include(admin.site.urls)),
)
