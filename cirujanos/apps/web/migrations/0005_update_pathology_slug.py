# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from south.db import db
from south.v2 import DataMigration
import datetime

class Migration(DataMigration):

    def forwards(self, orm):
        for pathology in orm.Pathology.objects.all():
            pathology.slug = slugify(pathology.name)
            pathology.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'web.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['web']
    symmetrical = True
