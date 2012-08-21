# -*- coding: utf-8 -*-

from apps.common.helpers import get_image_name
from md5 import md5

aaa = 'gallery/7d/7d0eab293e4b2008.jpg'
print '7d0eab293e4b2008'
print get_image_name(aaa)

print md5('111').hexdigest()