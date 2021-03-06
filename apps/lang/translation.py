# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from apps.flatpages.models import FlatPage
from apps.gallery.models import Albums, Gallery
from apps.menu.models import Menu
from apps.news.models import News

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class AlbumsTranslationOptions(TranslationOptions):
    fields = ('name',)


class GalleryTranslationOptions(TranslationOptions):
    fields = ('name', 'descr',)


class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_name', 'content',)


translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Albums, AlbumsTranslationOptions)
translator.register(Gallery, GalleryTranslationOptions)
translator.register(Menu, MenuTranslationOptions)
translator.register(News, NewsTranslationOptions)
