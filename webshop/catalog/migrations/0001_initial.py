# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.Category'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('catalog', ['Category'])

        # Adding model 'FeelName'
        db.create_table('Feel_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('catalog', ['FeelName'])

        # Adding model 'GiftPrice'
        db.create_table('gift_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('catalog', ['GiftPrice'])

        # Adding model 'Product'
        db.create_table('products', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('new_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2, blank=True)),
            ('not_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_bestseller', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_aqua', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('feel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.FeelName'], null=True, blank=True)),
            ('gift', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.GiftPrice'], null=True, blank=True)),
        ))
        db.send_create_signal('catalog', ['Product'])

        # Adding M2M table for field categories on 'Product'
        db.create_table('products_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('category', models.ForeignKey(orm['catalog.category'], null=False))
        ))
        db.create_unique('products_categories', ['product_id', 'category_id'])

        # Adding model 'ProductImage'
        db.create_table('product_images', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('catalog', ['ProductImage'])

        # Adding model 'CharacteristicType'
        db.create_table('characteristics_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('catalog', ['CharacteristicType'])

        # Adding unique constraint on 'CharacteristicType', fields ['name']
        db.create_unique('characteristics_type', ['name'])

        # Adding model 'Characteristic'
        db.create_table('characteristics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('characteristic_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.CharacteristicType'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
        ))
        db.send_create_signal('catalog', ['Characteristic'])

        # Adding unique constraint on 'Characteristic', fields ['product', 'characteristic_type']
        db.create_unique('characteristics', ['product_id', 'characteristic_type_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Characteristic', fields ['product', 'characteristic_type']
        db.delete_unique('characteristics', ['product_id', 'characteristic_type_id'])

        # Removing unique constraint on 'CharacteristicType', fields ['name']
        db.delete_unique('characteristics_type', ['name'])

        # Deleting model 'Category'
        db.delete_table('categories')

        # Deleting model 'FeelName'
        db.delete_table('Feel_product')

        # Deleting model 'GiftPrice'
        db.delete_table('gift_price')

        # Deleting model 'Product'
        db.delete_table('products')

        # Removing M2M table for field categories on 'Product'
        db.delete_table('products_categories')

        # Deleting model 'ProductImage'
        db.delete_table('product_images')

        # Deleting model 'CharacteristicType'
        db.delete_table('characteristics_type')

        # Deleting model 'Characteristic'
        db.delete_table('characteristics')


    models = {
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
        'catalog.feelname': {
            'Meta': {'object_name': 'FeelName', 'db_table': "'Feel_product'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'catalog.giftprice': {
            'Meta': {'object_name': 'GiftPrice', 'db_table': "'gift_price'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'catalog.product': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Product', 'db_table': "'products'"},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.FeelName']", 'null': 'True', 'blank': 'True'}),
            'gift': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.GiftPrice']", 'null': 'True', 'blank': 'True'}),
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