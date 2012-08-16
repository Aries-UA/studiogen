# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from apps.common.widgets import CKEditorAdmin

class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                                    " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                                            " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage
        widgets = {
            'content_ru': CKEditorAdmin(),
            'content_en': CKEditorAdmin(),
            'content_he': CKEditorAdmin(),
            'content_ua': CKEditorAdmin(),
        }


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_(u'SEO'), {'fields': ('keywords', 'description', 'copyright')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')


class TranslatedFlatPageAdmin(FlatPageAdmin, TranslationAdmin):

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
        field = super(TranslatedFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field


admin.site.register(FlatPage, TranslatedFlatPageAdmin)
