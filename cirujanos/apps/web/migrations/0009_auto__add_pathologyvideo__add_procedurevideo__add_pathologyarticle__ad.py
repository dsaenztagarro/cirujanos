# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PathologyVideo'
        db.create_table(u'web_pathologyvideo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pathology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Pathology'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Video'])),
            ('order', self.gf('django.db.models.fields.CharField')(default='A', max_length=3)),
        ))
        db.send_create_signal('web', ['PathologyVideo'])

        # Adding model 'ProcedureVideo'
        db.create_table(u'web_procedurevideo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Procedure'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Video'])),
            ('order', self.gf('django.db.models.fields.CharField')(default='A', max_length=3)),
        ))
        db.send_create_signal('web', ['ProcedureVideo'])

        # Adding model 'PathologyArticle'
        db.create_table(u'web_pathologyarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pathology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Pathology'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Article'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('web', ['PathologyArticle'])

        # Adding model 'ProcedureArticle'
        db.create_table(u'web_procedurearticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Procedure'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Article'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('web', ['ProcedureArticle'])


    def backwards(self, orm):
        # Deleting model 'PathologyVideo'
        db.delete_table(u'web_pathologyvideo')

        # Deleting model 'ProcedureVideo'
        db.delete_table(u'web_procedurevideo')

        # Deleting model 'PathologyArticle'
        db.delete_table(u'web_pathologyarticle')

        # Deleting model 'ProcedureArticle'
        db.delete_table(u'web_procedurearticle')


    models = {
        'media.article': {
            'Meta': {'object_name': 'Article'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.video': {
            'Meta': {'object_name': 'Video'},
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
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
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
            'meta_description': ('django.db.models.fields.TextField', [], {}),
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