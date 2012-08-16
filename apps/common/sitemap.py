# -*- coding: utf-8 -*-
import datetime
from django.contrib.sitemaps import Sitemap

class appSitemap(Sitemap):
	
    changefreq = "never"
    priority = 0.5

    def items(self):
        return (
            {'location': '/',},
            {'location': '/info/',},
            {'location': '/contacts/',},
            {'location': '/account/login/',},
            {'location': '/account/registration/',},
            {'location': '/account/forgot/',},
        )

    def location(self, obj):
        return obj['location']

    #def lastmod(self, obj):
    #    return obj['lastmod']
