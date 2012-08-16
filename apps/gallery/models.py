# -*- coding: utf-8 -*-

import os
from settings import *
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common.helpers import CropImg


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
    img = models.ImageField(_(u'Изображение'), upload_to=NAME_GALLERY, max_length=150, blank=False)
    sort_order = models.IntegerField(_(u'Сортировка'), blank=False, default=0)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Изображение')
        verbose_name_plural = _(u'Изображение')
        ordering = ('sort_order',)

    def save(self):
        super(Gallery, self).save()
        f = ''.join([MEDIA_ROOT, self.img.name])
        fnew = ''.join([MEDIA_ROOT, NAME_THUMBS_GALLERY, self.img.name])
        obj = CropImg(f, None, 10, 10, 10)
        obj.resize(THUMB_W, THUMB_H)
        obj.save(fnew)

    def preview_image_url(self):
        return '<a href="%s/"><img src="%s%s%s"/></a>' % (str(self.id), MEDIA_URL, NAME_THUMBS_GALLERY, self.img.name)
    preview_image_url.short_description = _('Изображение')
    preview_image_url.allow_tags = True
