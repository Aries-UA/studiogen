# -*- coding: utf-8 -*-

import os
from settings import *
from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.common.fields import ThumbImageField
from apps.common.helpers import get_image_admin_prefix, get_image_name


class News(models.Model):

    title = models.CharField(_(u'Заголовок'), max_length=100, blank=False, default='')
    img1 = ThumbImageField(
        upload_to=NAME_NEWS, 
        default='', 
        blank=False, 
        null=False,
        width=800,
        verbose_name=_(u'Изображение 1')
    )
    img2 = ThumbImageField(
        upload_to=NAME_NEWS, 
        default='', 
        blank=False, 
        null=False,
        width=800,
        verbose_name=_(u'Изображение 2')
    )
    img3 = ThumbImageField(
        upload_to=NAME_NEWS, 
        default='', 
        blank=False, 
        null=False,
        width=800,
        verbose_name=_(u'Изображение 3')
    )
    short_name = models.TextField(_(u'Короткий контент'), max_length=500, blank=False, default='')
    content = models.TextField(_(u'Контент'), blank=False, default='')
    created = models.DateTimeField(_(u'Создан'), auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')
        ordering = ('-created',)

    def original(self):
        name = get_image_name(self.img1.name)
        name = (self.img1.name).replace(name, '_'.join([name, '600x400']))
        return '{0}{1}'.format(MEDIA_URL, name)

    """ ВПАДЛУ ПИСАТЬ КОД - ТУПО КОПИРНУЛ!!! """
    def thumb(self, img):
        if img.name == '':
            return ''
        else:
            name = get_image_name(img.name)
            name = (img.name).replace(name, '_'.join([name, '103x62']))
            return '{0}{1}'.format(MEDIA_URL, name)

    def original(self, img):
        if img.name == '':
            return ''
        else:
            name = get_image_name(img.name)
            name = (img.name).replace(name, '_'.join([name, '600x400']))
            return '{0}{1}'.format(MEDIA_URL, name)

    """ Да бля знаю что не правильно!!! Впадлу же!!! """

    def original1(self):
        return self.original(self.img1)
    def original2(self):
        return self.original(self.img2)
    def original3(self):
        return self.original(self.img3)

    def thumb1(self):
        return self.thumb(self.img1)
    def thumb2(self):
        return self.thumb(self.img2)
    def thumb3(self):
        return self.thumb(self.img3)