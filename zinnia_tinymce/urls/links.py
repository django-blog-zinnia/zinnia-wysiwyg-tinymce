"""
URLs for list of links in TinyMCE
"""
from django.conf.urls import url
from django.conf.urls import patterns

from zinnia_tinymce.views import FileLinksView
from zinnia_tinymce.views import ImageLinksView
from zinnia_tinymce.views import EntryLinksView


urlpatterns = patterns(
    '',
    url(r'^links.js$',
        EntryLinksView.as_view(),
        name='tinymce-external-links'),
    url(r'^images.js$',
        ImageLinksView.as_view(),
        name='tinymce-external-images'),
    url(r'^files.js$',
        FileLinksView.as_view(),
        name='tinymce-external-files'),
)
