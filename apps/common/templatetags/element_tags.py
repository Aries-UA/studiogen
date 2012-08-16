# -*- coding: utf-8 -*-

from settings import LANGUAGES
from django import template
from django.utils import translation

register = template.Library()

@register.inclusion_tag('templatetags/header.html')
def header():
	return {'LANGUAGE_CODE': translation.get_language(),}

@register.inclusion_tag('templatetags/footer.html', takes_context=True)
def footer(context):
	user = context['request'].user
	if user.is_authenticated():
		return {
			'auth': user.is_authenticated() and True or False,
			'LANGUAGE_CODE': translation.get_language(),
		}

@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def menu(context):
	user = context['request'].user
	auth = user.is_authenticated()
	return {
		'auth': auth,
		'reg': auth and 'reg' or '',
		'LANGUAGE_CODE': translation.get_language(),
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
		'LANGUAGE_CODE': translation.get_language(),
	}

@register.inclusion_tag('templatetags/select_language.html')
def select_language():
	return {'LANGUAGES':LANGUAGES,}
