# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConfigParam'
        db.create_table(u'web_configparam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('param_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('param_value', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('web', ['ConfigParam'])

        # Adding model 'Pathology'
        db.create_table(u'web_pathology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal('web', ['Pathology'])

        # Adding model 'Procedure'
        db.create_table(u'web_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal('web', ['Procedure'])


    def backwards(self, orm):
        # Deleting model 'ConfigParam'
        db.delete_table(u'web_configparam')

        # Deleting model 'Pathology'
        db.delete_table(u'web_pathology')

        # Deleting model 'Procedure'
        db.delete_table(u'web_procedure')


    models = {
        'web.configparam': {
            'Meta': {'object_name': 'ConfigParam'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'param_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'param_value': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'web.pathology': {
            'Meta': {'object_name': 'Pathology'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'web.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['web']