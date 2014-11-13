"""
URLs for filebrowser in TinyMCE
"""
from django.conf.urls import url
from django.conf.urls import patterns

from zinnia_tinymce.views import EntryLinksView
from zinnia_tinymce.views import RemoveFileView
from zinnia_tinymce.views import FileBrowserView


urlpatterns = patterns(
    '',
    url(r'^links.js$',
        EntryLinksView.as_view(),
        name='tinymce-external-links'),
    url(r'^(?P<file_type>\w+)/$',
        FileBrowserView.as_view(),
        name='tinymce-filebrowser'),
    url(r'^(?P<file_type>\w+)/remove/(?P<pk>\d+)/$',
        RemoveFileView.as_view(),
        name='tinymce-filebrowser-remove')
)
