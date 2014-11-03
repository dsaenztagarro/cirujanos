# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ContactNotificationReceiver'
        db.rename_table(u'about_contactnotificationreceiver',
                        u'about_notificationemail')

    def backwards(self, orm):
        db.rename_table(u'about_notificationemail',
                        u'about_contactnotificationreceiver')


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
        },
        'about.notificationemail': {
            'Meta': {'object_name': 'NotificationEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['about']
