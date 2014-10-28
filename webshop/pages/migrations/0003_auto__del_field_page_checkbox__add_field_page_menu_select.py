# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.checkbox'
        db.delete_column('pages_page', 'checkbox')

        # Adding field 'Page.menu_select'
        db.add_column('pages_page', 'menu_select',
                      self.gf('django.db.models.fields.CharField')(default='useful', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Page.checkbox'
        db.add_column('pages_page', 'checkbox',
                      self.gf('django.db.models.fields.CharField')(default='useful', max_length=20),
                      keep_default=False)

        # Deleting field 'Page.menu_select'
        db.delete_column('pages_page', 'menu_select')


    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'menu_select': ('django.db.models.fields.CharField', [], {'default': "'useful'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {})
        }
    }

    complete_apps = ['pages']