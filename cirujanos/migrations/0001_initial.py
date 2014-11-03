# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('web_configparam', 'cirujanos_configparam')

    def backwards(self, orm):
        db.rename_table('cirujanos_configparam', 'web_configparam')


    models = {
        u'cirujanos.configparam': {
            'Meta': {'object_name': 'ConfigParam'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'param_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'param_value': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['cirujanos']
