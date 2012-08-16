# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from apps.flatpages.models import FlatPage
from apps.gallery.models import Albums, Gallery

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class AlbumsTranslationOptions(TranslationOptions):
    fields = ('name',)

class GalleryTranslationOptions(TranslationOptions):
    fields = ('name', 'descr',)


translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Albums, AlbumsTranslationOptions)
translator.register(Gallery, GalleryTranslationOptions)
