"""Test cases for zinnia-tinymce"""
from django.contrib.admin.sites import AdminSite
from django.test import RequestFactory
from django.test import TestCase

from zinnia.models.entry import Entry
from zinnia.signals import disconnect_entry_signals

from zinnia_tinymce.admin import EntryAdminTinyMCE


class BaseAdminTestCase(TestCase):

    def setUp(self):
        disconnect_entry_signals()
        self.site = AdminSite()
        self.admin = EntryAdminTinyMCE(
            Entry, self.site)


class EntryAdminTinyMCETestCase(BaseAdminTestCase):
    """Test case for Entry Admin with TinyMCE"""

    def setUp(self):
        super(EntryAdminTinyMCETestCase, self).setUp()
        self.request_factory = RequestFactory()
        self.request = self.request_factory.get('/')

    def test_medias(self):
        medias = self.admin.media
        self.assertEqual(
            medias._css, {})
        jss = [
            'admin/js/core.js',
            'tiny_mce/tiny_mce.js',
            'django_tinymce/init_tinymce.js',
            'textareas/admin/zinnia/entry/',
            'zinnia/filebrowser/callback.js'
        ]
        medias_string = '$'.join(medias._js)
        for js in jss:
            self.assertTrue(js in medias_string)
