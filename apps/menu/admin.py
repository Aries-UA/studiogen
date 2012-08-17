# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.menu.models import Menu

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ('name', 'url', 'sort_order',)
    list_display_links = ('name',)


class TranslatedMenuAdmin(MenuAdmin, TranslationAdmin):

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
        field = super(TranslatedMenuAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


admin.site.register(Menu, TranslatedMenuAdmin)
