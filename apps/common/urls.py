# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from apps.common.sitemap import appSitemap

sitemaps = {
    'app': appSitemap,
}

urlpatterns = patterns('',
    url(r'^$', 'apps.common.views.index'),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
