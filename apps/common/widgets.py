# -*- coding: utf-8 -*-

from settings import STATIC_URL, MEDIA_URL
from django.forms.widgets import Textarea, Select, TextInput, CheckboxInput, ClearableFileInput
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from apps.common.helpers import get_image_admin_prefix, get_image_name

class CKEditor(Textarea):

    class Media:
        js = ('/static/js/ckeditor/ckeditor.js',)

    def __init__(self, *args, **kwargs):
        super(CKEditor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        rendered = super(CKEditor, self).render(name, value, attrs)
        txt = """
            <script type="text/javascript"><!--
                jQuery(document).ready(
                    function () {
                        CKEDITOR.replace('id_%s', {height:"400", width:"687"});
                    }
                );
            //--></script>
        """ % name
        return mark_safe(' '.join([rendered, txt,]))


class CKEditorAdmin(Textarea):

    class Media:
        js = ('/static/js/ckeditor/ckeditor.js',)

    def __init__(self, *args, **kwargs):
        super(CKEditorAdmin, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        rendered = super(CKEditorAdmin, self).render(name, value, attrs)
        rendered = ''.join(['<br /><br />', rendered])
        txt = """
            <script type="text/javascript"><!--
                jQuery(document).ready(
                    function () {
                        CKEDITOR.replace('id_%s', {height:"400", width:"900"});
                    }
                );
            //--></script>
        """ % name
        return mark_safe(' '.join([rendered, txt,]))


class DatePicker(TextInput):

    def render(self, name, value, attrs=None):
        rendered = super(DatePicker, self).render(name, value, attrs)
        script = """
        <script type="text/javascript">
            $('#id_%s').datepicker({altFormat:'dd.mm.yyyy', buttonImage:'/static/images/calendar.gif'});
        </script>
        """ % name
        return mark_safe(' '.join([rendered, script]))


#class AdminImageFileWidget(AdminFileWidget):
class AdminImageFileWidget(ClearableFileInput):

    template_with_initial = u'''
        <p class="file-upload">
            %(initial_text)s: %(initial)s %(clear_template)s
            <br />
            %(input_text)s: %(input)s
        </p>
    '''
    template_with_clear = u'''
        <span class="clearable-file-input">
            %(clear)s <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>
        </span>
    '''

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = u'%(input)s'
        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)
        if value and hasattr(value, "url"):
            thumb_name = get_image_name(escape(value.url))
            thumb_name = escape(value.url).replace(thumb_name, '_'.join([thumb_name, '103x62']))
            template = self.template_with_initial
            substitutions['initial'] = u'<a href="{0}" target="_blank"><img src="{1}" title="" /></a>'.format(escape(value.url), thumb_name)
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)