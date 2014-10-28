# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.is_featured'
        db.delete_column('products', 'is_featured')


    def backwards(self, orm):
        # Adding field 'Product.is_featured'
        db.add_column('products', 'is_featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'catalog.brandname': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name',),)", 'object_name': 'BrandName', 'db_table': "'brand_name'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.category': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Category', 'db_table': "'categories'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalog.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'catalog.characteristic': {
            'Meta': {'ordering': "['characteristic_type', 'value']", 'unique_together': "(('product', 'characteristic_type'),)", 'object_name': 'Characteristic', 'db_table': "'characteristics'"},
            'characteristic_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.CharacteristicType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.characteristictype': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name',),)", 'object_name': 'CharacteristicType', 'db_table': "'characteristics_type'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.product': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Product', 'db_table': "'products'"},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.BrandName']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_aqua': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_bestseller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'new_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'not_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'catalog.productimage': {
            'Meta': {'object_name': 'ProductImage', 'db_table': "'product_images'"},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        }
    }

    complete_apps = ['catalog']