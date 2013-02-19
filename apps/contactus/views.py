# -*- coding: utf-8 -*-

from settings import *
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.utils.translation import ugettext as _
from apps.contactus.forms import ContactForm
from django.utils import translation

def contact(request):
    message = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_data = form.cleaned_data
            data = {
                'title': send_data['title'],
                'message': send_data['message'],
            }
            t = loader.get_template('contactus_mail.html')
            c = RequestContext(request, data)
            html = t.render(c)
            msg = EmailMessage(_(u'Контактная форма'), html, send_data['email'], [EMAIL_FROM])
            msg.content_subtype = "html"
            msg.send()
            message = _(u'Спасибо, что написали нам!')
            form = ContactForm()
    else:
        form = ContactForm()
    data = {
        'form': form,
        'message': message,
        'LANGUAGE_CODE': translation.get_language(),
    }
    return render(request, 'contactus_index.html', data)
