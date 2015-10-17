# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import zinnia_tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(max_length=35, verbose_name='file type', choices=[(b'image', 'Image'), (b'file', 'Document')])),
                ('uploaded_file', models.FileField(upload_to=zinnia_tinymce.models.upload_path, verbose_name='file / image')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
            ],
            options={
                'ordering': ['-creation_date'],
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
            bases=(models.Model,),
        ),
    ]
