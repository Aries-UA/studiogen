# -*- coding: utf-8 -*-

from settings import *
from django.template import RequestContext, loader
from apps.gallery.models import Gallery

class GalleryTemplate(object):

    def __init__(self, request):
        self.request = request

    def __unicode__(self):
        return u'%s' % self.render()

    def render(self):
        data = {
            'gallery': Gallery.objects.all(),
            'thumb': ''.join([MEDIA_URL, NAME_THUMBS_GALLERY]),
            'media': MEDIA_URL,
        }
        t = loader.get_template('gallery_carusel.html')
        c = RequestContext(self.request, data)
        return t.render(c)
