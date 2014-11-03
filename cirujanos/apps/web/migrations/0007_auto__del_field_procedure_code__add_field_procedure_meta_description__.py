# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Procedure.code'
        db.delete_column(u'web_procedure', 'code')

        # Adding field 'Procedure.meta_description'
        db.add_column(u'web_procedure', 'meta_description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Pathology.code'
        db.delete_column(u'web_pathology', 'code')

        # Adding field 'Pathology.meta_description'
        db.add_column(u'web_pathology', 'meta_description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Procedure.code'
        raise RuntimeError("Cannot reverse this migration. 'Procedure.code' and its values cannot be restored.")
        # Deleting field 'Procedure.meta_description'
        db.delete_column(u'web_procedure', 'meta_description')


        # User chose to not deal with backwards NULL issues for 'Pathology.code'
        raise RuntimeError("Cannot reverse this migration. 'Pathology.code' and its values cannot be restored.")
        # Deleting field 'Pathology.meta_description'
        db.delete_column(u'web_pathology', 'meta_description')


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
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'web.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['web']