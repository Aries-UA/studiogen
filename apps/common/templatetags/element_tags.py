# -*- coding: utf-8 -*-

from settings import LANGUAGES, STATIC_URL
from django import template
from apps.menu.models import Menu

register = template.Library()

def get_code():
	from django.utils import translation
	return translation.get_language()

@register.inclusion_tag('templatetags/header.html')
def header():
	return {
		'LANGUAGE_CODE': get_code(),
		'STATIC_URL': STATIC_URL,
	}

@register.inclusion_tag('templatetags/footer.html', takes_context=True)
def footer(context):
	user = context['request'].user
	return {
		'LANGUAGE_CODE': get_code(),
		'STATIC_URL': STATIC_URL,
	}

@register.inclusion_tag('templatetags/menu.html')
def menu():
	code = get_code()
	if code in ['ru', 'en']:
		menus = Menu.objects.all()
	else:
		menus = Menu.objects.all().order_by('-sort_order')
	td_width = 1
	if len(menus) > 0:
		td_width = int(99.99 / len(menus))
	return {
		'menus': menus,
		'td_width': td_width,
		'LANGUAGE_CODE': get_code(),
	}

@register.inclusion_tag('templatetags/head.html', takes_context=True)
def head(context):
	request = context['request']
	return {
		'title': request.HEAD.title,
		'keywords': request.HEAD.keywords,
		'description': request.HEAD.description,
		'copyright': request.HEAD.copyright,
		'domain': request.HEAD.domain,
		'LANGUAGE_CODE': get_code(),
		'STATIC_URL': STATIC_URL,
	}

@register.inclusion_tag('templatetags/select_language.html')
def select_language():
	return {'LANGUAGES':LANGUAGES,}

@register.filter
def style(selector):
	code = get_code()
	if code in ['ru', 'en']:
		return selector
	else:
		if selector == 'left':
			return 'right'
		else:
			return 'left'

