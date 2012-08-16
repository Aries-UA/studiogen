# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^account/registration/$', 'apps.account.views.registration'),
    (r'^account/registration/confirm/(?P<auth_key>[a-z,0-9]+)/$', 'apps.account.views.registration_confirm'),
    (r'^account/logout/$', 'apps.account.views.log_out'),
    (r'^account/login/$', 'apps.account.views.log_in'),
    (r'^account/forgot/$', 'apps.account.views.forgot'),
    (u'^account/profile/$', 'apps.account.views.profile'),
)
