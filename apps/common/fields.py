#! -*- coding: utf-8 -*-

from PIL import Image
import os
import datetime
from md5 import md5
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile
from StringIO import StringIO
from django.db import models
from settings import IMAGE_SIZE, MEDIA_ROOT
from apps.common.helpers import CropImg


class ThumbImageField(models.ImageField):

    def __init__(self, width='*', height='*', **kwargs):
        self.width = width
        self.height = height
        super(self.__class__, self).__init__(**kwargs)

    def save_form_data(self, instance, data):
        if data and isinstance(data, UploadedFile):
            instance.save()
            new_name = md5(str(datetime.datetime.now())).hexdigest()[5:21]
            upload_to = self.upload_to.split('/')
            self.upload_to = '/'.join([upload_to[0], new_name[0:2]])
            data.name = '.'.join([new_name, 'jpg'])
            pth = ''.join([MEDIA_ROOT, self.upload_to])
            if not os.path.isdir(pth):
                os.makedirs(pth)
            image = Image.open(data)
            for s in IMAGE_SIZE:
                fnew = ''.join([pth, '/', new_name, '_', str(s['w']), 'x', str(s['h']), '.jpg'])
                new_image = StringIO()
                image.save(new_image, 'JPEG', quality=90)
                res = SimpleUploadedFile(data.name, new_image.getvalue(), data.content_type)
                obj = CropImg(res=res, key=None)
                obj.quality = 90
                if s['crop']:
                    obj.resize_only(s['w'], s['h'])
                    obj.save(fnew)
                else:
                    obj.thumb(fnew, s['w'], s['h'])
                del(obj)
            image.thumbnail((self.width, self.height), Image.ANTIALIAS)
            new_image = StringIO()
            image.save(new_image, 'JPEG', quality=90)
            data = SimpleUploadedFile(data.name, new_image.getvalue(), data.content_type)
            self.delete_file(instance)
        super(ThumbImageField, self).save_form_data(instance, data)

    def delete_file(self, instance, *args, **kwargs):
        if getattr(instance, self.attname):
            image = getattr(instance, '%s' % self.name)
            file_name = image.path
            fl = {'%s__exact' % self.name: getattr(instance, self.attname)}
            if os.path.exists(file_name) and not instance.__class__._default_manager.filter(**fl).exclude(pk=instance._get_pk_val()):
                os.remove(file_name)
