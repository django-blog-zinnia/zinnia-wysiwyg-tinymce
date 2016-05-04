"""Defaults urls for the Zinnia TinyMCE"""
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^', include('zinnia_tinymce.urls.links')),
    url(r'^filebrowser/', include('zinnia_tinymce.urls.filebrowser')),
]
