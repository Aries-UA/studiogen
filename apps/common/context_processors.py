# -*- coding: utf-8 -*-

def base_layout(request):
    from django.utils import translation
    
    code = translation.get_language()
    if code in ['ru', 'en']:
        data = {'BASE_LAYOUT': 'layout_ru.html',}
    else:
        data = {'BASE_LAYOUT': 'layout_ru.html',}
    return data