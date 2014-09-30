======================
zinnia-wysiwyg-tinymce
======================

Zinnia-wysiwyg-tinymce is a package allowing you to edit your entries
with `TinyMCE`_, including a dedicated filebrowser plugin.

Installation
============

* Install the package on your system: ::

  $ pip install zinnia-wysiwyg-tinymce

  `django-tinymce`_ and `sorl-thumbnail`_ will also be installed as
  dependencies if they are not already present on the system.

* Install and configure in your project django-tinymce and sorl-thumbnail
  accordingly to their documentation:

  - http://django-tinymce.readthedocs.org/en/latest/installation.html
  - http://sorl-thumbnail.readthedocs.org/en/latest/installation.html

* Register the ``'zinnia_tinymce'`` in your ``INSTALLED_APPS`` after the
  ``'zinnia'`` application.

* Include this URLset into your project's urls.py: ::

    url(r'^tinymce/filebrowser/', include('zinnia_tinymce.urls')),

You are done !

TinyMCE can be customized by overriding the
``admin/zinnia/entry/tinymce_textareas.js`` template.

.. _TinyMCE: http://www.tinymce.com/
.. _django-tinymce: https://github.com/aljosa/django-tinymce
.. _sorl-thumbnail: https://github.com/mariocesar/sorl-thumbnail
