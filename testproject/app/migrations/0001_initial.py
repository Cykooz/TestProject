# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'users'
        db.create_table('app_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('app', ['users'])

        # Adding model 'rooms'
        db.create_table('app_rooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('app', ['rooms'])


    def backwards(self, orm):
        
        # Deleting model 'users'
        db.delete_table('app_users')

        # Deleting model 'rooms'
        db.delete_table('app_rooms')


    models = {
        'app.rooms': {
            'Meta': {'object_name': 'rooms'},
            'department': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'app.users': {
            'Meta': {'object_name': 'users'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['app']
