from django.db import models
from django.db import migrations

import zinnia_tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('file_type', models.CharField(
                    max_length=35, verbose_name='file type',
                    choices=[('image', 'Image'), ('file', 'Document')])),
                ('uploaded_file', models.FileField(
                    upload_to=zinnia_tinymce.models.upload_path,
                    verbose_name='file / image')),
                ('creation_date', models.DateTimeField(
                    auto_now_add=True, verbose_name='creation date')),
            ],
            options={
                'ordering': ['-creation_date'],
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
            bases=(models.Model,),
        ),
    ]
