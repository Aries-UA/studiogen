# -*- coding: utf-8 -*-
import re

from django import forms
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from settings import *


class FormErrorList(ErrorList):
    
    def __unicode__(self):
        return self.as_tr()

    def as_tr(self):
        if not self:
            return u''
        return u'%s' % ''.join([u'<tr><td colspan="2" width="335" class="tr_error">%s</td></tr>' % e for e in self])


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.error_class = FormErrorList

    def as_table(self):
        normal_row = u'''
        %(errors)s
        <tr>
            <td%(html_class_attr)s width="95">
                %(label)s
            </td>
            <td>
                %(field)s
                %(help_text)s
            </td>
        </tr>
        '''
        return self._html_output(
            normal_row = normal_row,
            error_row = u'%s',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False
        )


class ContactForm(BaseForm):

    email = forms.EmailField(label=_(u'Email'), min_length=3, max_length=100, required=True, initial='')
    title = forms.CharField(label=_(u"Тема"), min_length=5, max_length=100, required=True, initial='')
    message = forms.CharField(label=_(u"Сообщение"), widget=forms.Textarea, min_length=5, max_length=500, required=True, initial='')

    def clean_title(self):
        name = self.cleaned_data['title']
        if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(name):
            raise forms.ValidationError(_(u'Некорректные символы. Допустимы буквы, цифры, пробел, а также "-", ",", "."'))
        else:
            return name

    def clean_message(self):
        name = self.cleaned_data['message']
        if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(name):
            raise forms.ValidationError(_(u'Некорректные символы. Допустимы буквы, цифры, пробел, а также "-", ",", "."'))
        else:
            return name

