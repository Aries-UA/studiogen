# -*- coding: utf-8 -*-

import os
from settings import *
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common.fields import ThumbImageField
from apps.common.helpers import get_image_admin_prefix, get_image_name


class Albums(models.Model):

    name = models.CharField(_(u'Название'), max_length=100, blank=False, default='')
    sort_order = models.IntegerField(_(u'Сортировка'), blank=False, default=0)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Альбом')
        verbose_name_plural = _(u'Альбомы')
        ordering = ('sort_order',)


class Gallery(models.Model):

    album = models.ForeignKey(Albums, blank=False, verbose_name=_(u'Альбом'))
    name = models.CharField(_(u'Название'), max_length=100, blank=True, default='')
    descr = models.CharField(_(u'Описание'), blank=True, default='', max_length=500)
    img = ThumbImageField(
        upload_to=NAME_GALLERY, 
        default='', 
        blank=False, 
        null=False,
        width=800,
        verbose_name=_(u'Изображение')
    )
    sort_order = models.IntegerField(_(u'Сортировка'), blank=False, default=0)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Изображение')
        verbose_name_plural = _(u'Изображение')
        ordering = ('sort_order',)

    def preview_image_url(self):
        pref = get_image_admin_prefix()
        name = get_image_name(self.img.name)
        name = (self.img.name).replace(name, '_'.join([name, pref]))
        return '<a href="{0}/"><img src="{1}{2}"/></a>'.format(str(self.id), MEDIA_URL, name)
    preview_image_url.short_description = _('Изображение')
    preview_image_url.allow_tags = True

    def original(self):
        name = get_image_name(self.img.name)
        name = (self.img.name).replace(name, '_'.join([name, '600x400']))
        return '{0}{1}'.format(MEDIA_URL, name)

    def thumb(self):
        name = get_image_name(self.img.name)
        name = (self.img.name).replace(name, '_'.join([name, '103x62']))
        return '{0}{1}'.format(MEDIA_URL, name)