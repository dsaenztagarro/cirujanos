# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Procedure.slug'
        db.add_column(u'web_procedure', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='procedure', max_length=100),
                      keep_default=False)

        # Adding field 'Pathology.slug'
        db.add_column(u'web_pathology', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='pathology', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Procedure.slug'
        db.delete_column(u'web_procedure', 'slug')

        # Deleting field 'Pathology.slug'
        db.delete_column(u'web_pathology', 'slug')


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
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'web.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['web']