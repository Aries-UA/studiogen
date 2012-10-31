# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.gallery.models import Albums, Gallery
from apps.common.widgets import AdminImageFileWidget

class AlbumsForm(forms.ModelForm):

    class Meta:
        model = Albums


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        widgets = {
            'img': AdminImageFileWidget(),
        }


class AlbumsAdmin(admin.ModelAdmin):
    form = AlbumsForm
    list_display = ('name', 'sort_order',)
    list_display_links = ('name',)


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    fieldsets = (
        (u'Изображение', {'fields': ('img',)}),
        (u'Альбом', {'fields': ('album',)}),
        (u'Описание', {'fields': ('name', 'descr')}),
    )
    list_display = ('preview_image_url', 'name', 'album', 'descr', 'sort_order')
    list_display_links = ('preview_image_url', 'name')
    ordering = ('album', 'sort_order')


class TranslatedAlbumsAdmin(AlbumsAdmin, TranslationAdmin):

    class Media:
        js = (
            '/static/js/force_jquery.js',
            '/static/js/jquery-ui.min.js',
            '/static/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/css/tabbed_translation_fields.css',),
        }
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedAlbumsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


class TranslatedGalleryAdmin(GalleryAdmin, TranslationAdmin):

    class Media:
        js = (
            '/static/js/force_jquery.js',
            '/static/js/jquery-ui.min.js',
            '/static/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/css/tabbed_translation_fields.css',),
        }
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedGalleryAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


admin.site.register(Albums, TranslatedAlbumsAdmin)
admin.site.register(Gallery, TranslatedGalleryAdmin)
