# -*- coding: utf-8 -*-

from settings import STATIC_URL
from django.forms.widgets import Textarea, Select, TextInput
from django.utils.safestring import mark_safe
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode

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
