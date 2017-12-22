from django import template
from django.utils import translation
import json
import re
register = template.Library()

@register.simple_tag
def translate(en, zh, zh_hant):
    lang = translation.get_language().replace('-', '_')
    return eval(lang)

@register.simple_tag
def get_lang():
    return translation.get_language()

@register.simple_tag
def get_lang_():
    return translation.get_language().replace('-', '_')

@register.simple_tag
def filter_tag(html_str):
    return re.compile(r'<[^>]+>', re.S).sub('', html_str)

@register.simple_tag
def format_time(date_obj, format):
    return str(date_obj.strftime(format))