# -*- coding: utf-8 -*-

import os
from settings import *
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Menu(models.Model):

    name = models.CharField(_(u'Название'), max_length=100, blank=False, default='')
    url = models.CharField(_(u'Линк'), max_length=100, blank=False, default='')
    sort_order = models.IntegerField(_(u'Сортировка'), blank=False, default=0)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Меню')
        verbose_name_plural = _(u'Меню')
        ordering = ('sort_order',)
