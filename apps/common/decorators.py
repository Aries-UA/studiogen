# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

def pagins_page(limit_row_page, available_limit_row):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            try:
                page = int(request.GET.get('page', 1))
            except:
                page = 1
            page = page - 1
            try:
                limit = int(request.GET.get('limit', limit_row_page))
                if limit not in available_limit_row:
                    limit = limit_row_page
            except:
                limit = limit_row_page
            output = func(request, page=page, limit=limit)
            return output
        return wrapper
    return decorator

def permission_views(perm, go_page):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated() and user.has_perm(perm):
                return func(request, *args, **kwargs)
            else:
                messages.error(request, _(u'Доступ к запрашиваемой странице запрещен'))
                return HttpResponseRedirect(reverse(go_page))
        return wrapper
    return decorator
