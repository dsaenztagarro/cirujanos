# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('home', '0002_create_slider'),
    )

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

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
