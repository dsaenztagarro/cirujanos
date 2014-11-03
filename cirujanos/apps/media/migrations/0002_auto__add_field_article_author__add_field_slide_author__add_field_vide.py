# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.author'
        db.add_column(u'media_article', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=250),
                      keep_default=False)

        # Adding field 'Slide.author'
        db.add_column(u'media_slide', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=250),
                      keep_default=False)

        # Adding field 'Video.author'
        db.add_column(u'media_video', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=250),
                      keep_default=False)

        # Adding field 'Event.author'
        db.add_column(u'media_event', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.author'
        db.delete_column(u'media_article', 'author')

        # Deleting field 'Slide.author'
        db.delete_column(u'media_slide', 'author')

        # Deleting field 'Video.author'
        db.delete_column(u'media_video', 'author')

        # Deleting field 'Event.author'
        db.delete_column(u'media_event', 'author')


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
        'media.event': {
            'Meta': {'object_name': 'Event'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media.slide': {
            'Meta': {'object_name': 'Slide'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
        }
    }

    complete_apps = ['media']