# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.news.models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model = News


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('title', 'short_name', 'created',)
    list_display_links = ('title',)


class TranslatedNewsAdmin(NewsAdmin, TranslationAdmin):

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
        field = super(TranslatedNewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


admin.site.register(News, TranslatedNewsAdmin)