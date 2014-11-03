# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.order'
        db.add_column(u'home_post', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Post.public'
        db.add_column(u'home_post', 'public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Post.publish_date'
        db.add_column(u'home_post', 'publish_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today),
                      keep_default=False)


        # Changing field 'Post.system_image_path'
        db.alter_column(u'home_post', 'system_image_path', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Post.link'
        db.alter_column(u'home_post', 'link', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Post.order'
        db.delete_column(u'home_post', 'order')

        # Deleting field 'Post.public'
        db.delete_column(u'home_post', 'public')

        # Deleting field 'Post.publish_date'
        db.delete_column(u'home_post', 'publish_date')


        # Changing field 'Post.system_image_path'
        db.alter_column(u'home_post', 'system_image_path', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Post.link'
        db.alter_column(u'home_post', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'home.post': {
            'Meta': {'object_name': 'Post'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'/home/vagrant/Development/projects/cirujanos/www/static/images/home/posts/default.jpg'", 'max_length': '100'}),
            'is_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'system_image_path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'home.slider': {
            'Meta': {'object_name': 'Slider'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['home']