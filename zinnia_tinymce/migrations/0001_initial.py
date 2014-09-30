from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileModel'
        db.create_table(u'zinnia_tinymce_filemodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_type', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('uploaded_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'zinnia_tinymce', ['FileModel'])

    def backwards(self, orm):
        # Deleting model 'FileModel'
        db.delete_table(u'zinnia_tinymce_filemodel')

    models = {
        'zinnia_tinymce.filemodel': {
            'Meta': {'ordering': "['-creation_date']", 'object_name': 'FileModel'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['zinnia_tinymce']
