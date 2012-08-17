# -*- coding: utf-8 -*-

import os
from settings import *
from django.db import models
from django.utils.translation import ugettext_lazy as _


class News(models.Model):

    title = models.CharField(_(u'Заголовок'), max_length=100, blank=False, default='')
    short_name = models.TextField(_(u'Короткий контент'), max_length=500, blank=False, default='')
    content = models.TextField(_(u'Контент'), blank=False, default='')
    created = models.DateTimeField(_(u'Создан'), auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')
        ordering = ('-created',)
