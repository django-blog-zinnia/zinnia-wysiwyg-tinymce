"""
URLs for filebrowser in TinyMCE
"""
from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic import View

from zinnia_tinymce.views import RemoveFileView
from zinnia_tinymce.views import FileBrowserView
from zinnia_tinymce.views import FileBrowserCallBackView


urlpatterns = patterns(
    '',
    url(r'^$',
        View.as_view(),
        name='tinymce-filebrowser-dispatch'),
    url(r'^callback.js$',
        FileBrowserCallBackView.as_view(),
        name='tinymce-filebrowser-callback'),
    url(r'^(?P<file_type>\w+)/$',
        FileBrowserView.as_view(),
        name='tinymce-filebrowser'),
    url(r'^(?P<file_type>\w+)/remove/(?P<pk>\d+)/$',
        RemoveFileView.as_view(),
        name='tinymce-filebrowser-remove')
)
