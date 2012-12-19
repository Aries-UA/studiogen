# -*- coding: utf-8 -*-

from settings import *
from django.shortcuts import render
from django.template import RequestContext, loader
from django.utils import translation

from apps.gallery.models import Albums, Gallery

def album(request):
    try:
        album_id = int(request.GET.get('album', 0))
    except:
        album_id = 0
    if Albums.objects.filter(id=album_id).exists():
        album = Albums.objects.get(pk=album_id)
    else:
        try:
            album = Albums.objects.all()[0]
        except:
            album = None
    gallery = Gallery.objects.filter(album=album)
    try:
        big = gallery[0]
    except:
        big = False
    request.HEAD.setHead('/gallery_info/')
    data = {
        'html': request.HEAD.content,
        'albums': Albums.objects.all(),
        'gallery': gallery,
        'big': big,
        'LANGUAGE_CODE': translation.get_language(),
    }
    return render(request, 'gallery_albums.html', data)
