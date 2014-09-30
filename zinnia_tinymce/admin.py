"""EntryAdmin for zinnia-tinymce"""
from django.forms import Media
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

from tinymce.widgets import TinyMCE

from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin


class EntryAdminTinyMCEMixin(object):
    """
    Mixin adding TinyMCE for editing Entry.content field.
    """

    def _media(self):
        """
        The medias needed to enhance the admin page.
        """
        media = super(EntryAdminTinyMCEMixin, self).media

        media += TinyMCE().media + Media(
            js=[reverse('tinymce-js', args=['admin/zinnia/entry']),
                staticfiles_storage.url(
                    'zinnia_tinymce/js/filebrowser.js')]
        )

        return media
    media = property(_media)


class EntryAdminTinyMCE(EntryAdminTinyMCEMixin,
                        EntryAdmin):
    """
    Enrich the default EntryAdmin with TinyMCE.
    """
    pass

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdminTinyMCE)
