#!/usr/bin/env python
from urllib import request
from xml.dom.minidom import parseString
from urllib.error import HTTPError, URLError
import socket
from django.db.models.loading import get_app 

DOMAIN = 'http://mygululu.com/'
SITEMAP_URL = DOMAIN + 'sitemap.xml?v=1'
TIMEOUT = 2

def check_urls(urls):
    for url in urls:
        try:
            result = request.urlopen(url, timeout=TIMEOUT).getcode()
        except Exception as e:
            result = e
        if result is 200:
            print('\033[1;36m',  str(result), '\033[0m', url)
        else:
            print('\033[1;31m',  str(result), '\033[0m', url)

def get_sitemap_urls():
    response = request.urlopen(SITEMAP_URL)
    sitemap_xml=response.read()
    dom = parseString(sitemap_xml)
    root = dom.documentElement
    url_tags = root.getElementsByTagName("url")
    urls = []
    for tag in url_tags:
        urls.append(tag.getElementsByTagName('loc')[0].childNodes[0].data)
    return urls

def get_blog_urls():
    import sys, os
    import django
    sys.path.append('')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'
    django.setup()
    from  aldryn_newsblog.models import ArticleTranslation

    arts = ArticleTranslation.objects.all()
    urls = []
    for art in arts:
        urls.append(DOMAIN + 'blog/' +art.slug)
    return urls

if __name__ == '__main__':
    check_urls(get_sitemap_urls())
    check_urls(get_blog_urls())
