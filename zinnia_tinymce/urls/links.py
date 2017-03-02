"""
URLs for list of links in TinyMCE
"""
from django.conf.urls import url

from zinnia_tinymce.views import EntryLinksView
from zinnia_tinymce.views import FileLinksView
from zinnia_tinymce.views import ImageLinksView


urlpatterns = [
    url(r'^links.js$',
        EntryLinksView.as_view(),
        name='tinymce-external-links'),
    url(r'^images.js$',
        ImageLinksView.as_view(),
        name='tinymce-external-images'),
    url(r'^files.js$',
        FileLinksView.as_view(),
        name='tinymce-external-files'),
]
