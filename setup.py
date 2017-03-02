"""Setup script of zinnia-wysiwyg-tinymce"""
from setuptools import find_packages
from setuptools import setup

import zinnia_tinymce

setup(
    name='zinnia-wysiwyg-tinymce',
    version=zinnia_tinymce.__version__,

    description='TinyMCE for editing entries in django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, zinnia, wysiwyg, tinymce',

    author=zinnia_tinymce.__author__,
    author_email=zinnia_tinymce.__email__,
    url=zinnia_tinymce.__url__,

    packages=find_packages(exclude=['demo_zinnia_tinymce']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_tinymce.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-tinymce',
                      'sorl-thumbnail']
)
