# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from aldryn_newsblog.sitemaps import NewsBlogSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from web.views import redirect_views
from web.views import redirect_blogs
from web.views import status_views
from django.shortcuts import redirect
from django.http import HttpResponse

admin.autodiscover()
urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap, 'blog_pages':NewsBlogSitemap}}),
    url(r'^app/download/gululu/$', redirect_views.redirect_download_app_no_cdn),
    url(r'^app/download/$', redirect_views.redirect_download_app),
    url(r'^play/$', redirect_views.redirect_index),
    url(r'^setup/$', redirect_views.redirect_faq),
    url(r'^support/$', redirect_views.redirect_faq),
    url(r'^shop/(.+)/$', redirect_views.redirect_shop_channel),
    url(r'^shop/$', redirect_views.redirect_shop),
    url(r'^srvacl/$', status_views.status_views, name="serverAccessLog"),
    url(r'^srverr/$', status_views.status_views, name="serverErrorLog"),
    url(r'^robots\.txt$', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file")
]

redirect_blogs.add_blog_urls(urlpatterns)

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
