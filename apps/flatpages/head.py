# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site
from apps.flatpages.models import FlatPage

class Head(object):

    title = u'Studiogen'
    keywords = ''
    description = ''
    copyright = ''
    domain = ''
    content = ''

    def __init__(self):
        self.domain = Site.objects.get_current().name

    def setHead(self, url=''):
        if FlatPage.objects.filter(url__exact=url, sites__id__exact=settings.SITE_ID).exists():
            f = FlatPage.objects.get(url__exact=url, sites__id__exact=settings.SITE_ID)
            self.title = f.title
            self.keywords = f.keywords
            self.description = f.description
            self.copyright = f.copyright
            self.content = f.content
        else:
            self.title = u'Studiogen'
            self.keywords = ''
            self.description = ''
            self.copyright = ''
            self.content = ''
