# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table(u'about_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('about', ['Doctor'])

        # Adding model 'DoctorContent'
        db.create_table(u'about_doctorcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about.Doctor'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about.DoctorContentType'])),
            ('content_preview', self.gf('tinymce.models.HTMLField')()),
            ('content_details', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal('about', ['DoctorContent'])

        # Adding model 'DoctorContentType'
        db.create_table(u'about_doctorcontenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('about', ['DoctorContentType'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table(u'about_doctor')

        # Deleting model 'DoctorContent'
        db.delete_table(u'about_doctorcontent')

        # Deleting model 'DoctorContentType'
        db.delete_table(u'about_doctorcontenttype')


    models = {
        'about.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'about.doctorcontent': {
            'Meta': {'object_name': 'DoctorContent'},
            'content_details': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_preview': ('tinymce.models.HTMLField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['about.DoctorContentType']"}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['about.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'about.doctorcontenttype': {
            'Meta': {'object_name': 'DoctorContentType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['about']