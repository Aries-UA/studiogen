# -*- coding: utf-8 -*-

import os
import sys
import site

path = '/home/studiogen/data/www/studiogen/'
test = 'toggle_server1123'

if path not in sys.path:
    sys.path.append(path)

site.addsitedir('/home/studiogen/data/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()