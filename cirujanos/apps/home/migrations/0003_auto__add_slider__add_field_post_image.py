# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.send_create_signal(u'home', ['Slider'])

        # Adding field 'Post.image'
        db.add_column(u'home_post', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='/home/vagrant/Development/projects/cirujanos/www/static/images/post/default.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.image'
        db.delete_column(u'home_post', 'image')


    models = {
        u'home.post': {
            'Meta': {'object_name': 'Post'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'/home/vagrant/Development/projects/cirujanos/www/static/images/post/default.jpg'", 'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
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
