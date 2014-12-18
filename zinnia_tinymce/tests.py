"""Test cases for zinnia-tinymce"""
from django.test import TestCase
from django.test import RequestFactory
from django.contrib.admin.sites import AdminSite

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
        self.assertEqual(
            medias._js,
            ['/static/admin/js/core.js',
             '/static/admin/js/admin/RelatedObjectLookups.js',
             '/static/admin/js/jquery.min.js',
             '/static/admin/js/jquery.init.js',
             '/static/admin/js/actions.min.js',
             '/static/admin/js/urlify.js',
             '/static/admin/js/prepopulate.min.js',
             '/static/tiny_mce/tiny_mce.js',
             'django_tinymce/init_tinymce.js',
             '/tinymce/js/textareas/admin/zinnia/entry/',
             '/tinymce/zinnia/filebrowser/callback.js'])
