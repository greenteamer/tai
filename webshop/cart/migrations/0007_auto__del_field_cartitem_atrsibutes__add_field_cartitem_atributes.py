# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CartItem.atrsibutes'
        db.delete_column('cart_items', 'atrsibutes_id')

        # Adding field 'CartItem.atributes'
        db.add_column('cart_items', 'atributes',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['catalog.ProductVolume']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'CartItem.atrsibutes'
        db.add_column('cart_items', 'atrsibutes',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['catalog.ProductVolume']),
                      keep_default=False)

        # Deleting field 'CartItem.atributes'
        db.delete_column('cart_items', 'atributes_id')


    models = {
        'cart.cartitem': {
            'Meta': {'ordering': "['date_added']", 'object_name': 'CartItem', 'db_table': "'cart_items'"},
            'atributes': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ProductVolume']"}),
            'cart_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cupon': ('django.db.models.fields.related.ForeignKey', [], {'default': '2', 'to': "orm['catalog.Cupon']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feel': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['catalog.FeelName']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'catalog.brandname': {
            'Meta': {'object_name': 'BrandName', 'db_table': "'brand_product'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.category': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Category', 'db_table': "'categories'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalog.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'catalog.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'percent': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'catalog.feelname': {
            'Meta': {'object_name': 'FeelName', 'db_table': "'Feel_product'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.product': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Product', 'db_table': "'products'"},
            'brand_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.BrandName']", 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feel': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['catalog.FeelName']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_aqua': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_bestseller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'new_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'not_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'catalog.productvolume': {
            'Meta': {'object_name': 'ProductVolume', 'db_table': "'product_volume'"},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        }
    }

    complete_apps = ['cart']