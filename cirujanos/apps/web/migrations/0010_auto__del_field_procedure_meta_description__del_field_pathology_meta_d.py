# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Procedure.meta_description'
        db.delete_column(u'web_procedure', 'meta_description')

        # Deleting field 'Pathology.meta_description'
        db.delete_column(u'web_pathology', 'meta_description')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Procedure.meta_description'
        raise RuntimeError("Cannot reverse this migration. 'Procedure.meta_description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Pathology.meta_description'
        raise RuntimeError("Cannot reverse this migration. 'Pathology.meta_description' and its values cannot be restored.")

    models = {
        'media.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.video': {
            'Meta': {'object_name': 'Video'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'web.pathology': {
            'Meta': {'object_name': 'Pathology'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['media.Article']", 'through': "orm['web.PathologyArticle']", 'symmetrical': 'False'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['media.Video']", 'through': "orm['web.PathologyVideo']", 'symmetrical': 'False'})
        },
        'web.pathologyarticle': {
            'Meta': {'object_name': 'PathologyArticle'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pathology': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Pathology']"})
        },
        'web.pathologyvideo': {
            'Meta': {'object_name': 'PathologyVideo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '3'}),
            'pathology': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Pathology']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Video']"})
        },
        'web.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['media.Article']", 'through': "orm['web.ProcedureArticle']", 'symmetrical': 'False'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['media.Video']", 'through': "orm['web.ProcedureVideo']", 'symmetrical': 'False'})
        },
        'web.procedurearticle': {
            'Meta': {'object_name': 'ProcedureArticle'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Procedure']"})
        },
        'web.procedurevideo': {
            'Meta': {'object_name': 'ProcedureVideo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '3'}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Procedure']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Video']"})
        }
    }

    complete_apps = ['web']