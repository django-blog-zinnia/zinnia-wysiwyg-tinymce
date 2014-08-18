======================
zinnia-wysiwyg-tinymce
======================

Zinnia-wysiwyg-tinymce is a package allowing you to edit your entries
with `TinyMCE`_.

Installation
============

* Install the package on your system: ::

  $ pip install zinnia-wysiwyg-tinymce

  `django-tinymce`_ will also be installed as a dependency if not present.
  In this case also follow the `install instruction of django-tinymce`_ before
  going further.

* Register the ``'zinnia_tinymce'`` in your ``INSTALLED_APPS`` after the
  ``'zinnia'`` application.

You are done !

TinyMCE can be customized by overriding the
``admin/zinnia/entry/tinymce_textareas.js`` template.

.. _TinyMCE: http://www.tinymce.com/
.. _django-tinymce: https://github.com/aljosa/django-tinymce
.. _install instruction of django-tinymce: http://django-tinymce.readthedocs.org/en/latest/installation.html#id2
