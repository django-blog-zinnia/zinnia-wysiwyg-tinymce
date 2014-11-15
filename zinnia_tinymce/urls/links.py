"""
URLs for links in TinyMCE
"""
from django.conf.urls import url
from django.conf.urls import patterns

from zinnia_tinymce.views import EntryLinksView


urlpatterns = patterns(
    '',
    url(r'^links.js$',
        EntryLinksView.as_view(),
        name='tinymce-external-links'),
)
