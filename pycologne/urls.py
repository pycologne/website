# -*- coding: utf-8 -*-
"""URLs for the website."""

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('pycologne.events.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
        }
    }),
    url(r'^login/$', 'django.contrib.auth.views.login', {
       'template_name': 'website/login.html'
    }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
       'next_page': '/'
    }),                   
    url(r'^user/', include('userprofiles.urls')),
    url(r'^', include('cms.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += (
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,}),
    )
