# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0440\u0435\u043d\u0434\u0430')),
            ],
            options={
                'db_table': 'brand_product',
                'verbose_name_plural': '\u0411\u0440\u0435\u043d\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Slug for product url created from name.', unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta keywords', blank=True)),
                ('meta_description', models.CharField(help_text='Content for description meta tags', max_length=255, verbose_name='Meta description', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='catalog.Category', help_text='Parent-category for current category', null=True, verbose_name='Parent category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
            options={
                'ordering': ['characteristic_type', 'value'],
                'db_table': 'characteristics',
                'verbose_name_plural': 'Characteristics',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'characteristics_type',
                'verbose_name_plural': 'Characteristics Types',
            },
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u043f\u043e\u043d\u0430')),
                ('identifier', models.CharField(max_length=256, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440')),
                ('percent', models.CharField(max_length=10, verbose_name='\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0441\u043a\u0438\u0434\u043a\u0438')),
            ],
            options={
                'verbose_name_plural': '\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043a\u0443\u043f\u043e\u043d\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='FeelName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0412\u043a\u0443\u0441')),
            ],
            options={
                'db_table': 'Feel_product',
                'verbose_name_plural': '\u0412\u043a\u0443\u0441',
            },
        ),
        migrations.CreateModel(
            name='GiftPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0430\u0440\u043a\u0430')),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=9, decimal_places=2)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'gifts/images/', verbose_name='\u0424\u043e\u0442\u043e \u043f\u043e\u0434\u0430\u0440\u043a\u0430')),
                ('weight', models.DecimalField(verbose_name='\u0412\u0435\u0441', max_digits=9, decimal_places=2)),
            ],
            options={
                'ordering': ['-price'],
                'db_table': 'gift_price',
                'verbose_name_plural': '\u041f\u043e\u0434\u0430\u0440\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True, max_length=255, verbose_name='Slug')),
                ('not_available', models.BooleanField(verbose_name='\u041d\u0435\u0442 \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='\u041b\u0443\u0447\u0448\u0438\u0435 \u043f\u0440\u043e\u0434\u0430\u0436\u0438')),
                ('is_aqua', models.BooleanField(verbose_name='\u0416\u0438\u0434\u043a\u043e\u0441\u0442\u044c')),
                ('is_new', models.BooleanField(verbose_name='\u041d\u043e\u0432\u0438\u043d\u043a\u0430')),
                ('description', ckeditor.fields.RichTextField()),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta keywords', blank=True)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta description', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('brand_name', models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0440\u0435\u043d\u0434\u0430', blank=True, to='catalog.BrandName', null=True)),
                ('categories', models.ManyToManyField(help_text='Categories for product', to='catalog.Category', verbose_name='Categories')),
                ('feel', models.ManyToManyField(to='catalog.FeelName', null=True, verbose_name='\u0412\u043a\u0443\u0441', blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(help_text=b'Product image', upload_to=b'products/images/', verbose_name='Image')),
                ('description', models.CharField(max_length=255, verbose_name='Description', blank=True)),
                ('default', models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e')),
                ('product', models.ForeignKey(verbose_name='Product', to='catalog.Product', help_text='Referenced product')),
            ],
            options={
                'db_table': 'product_images',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='ProductVolume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.DecimalField(verbose_name='\u041e\u0431\u044a\u0435\u043c', max_digits=9, decimal_places=2)),
                ('weight', models.DecimalField(verbose_name='\u0412\u0435\u0441', max_digits=9, decimal_places=2)),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=9, decimal_places=2)),
                ('new_price', models.DecimalField(default=0.0, verbose_name='\u041d\u043e\u0432\u0430\u044f \u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2, blank=True)),
                ('default', models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043d\u0430\u0431\u043e\u0440')),
                ('product', models.ForeignKey(verbose_name='Product', to='catalog.Product', help_text='Referenced product')),
            ],
            options={
                'db_table': 'product_volume',
                'verbose_name_plural': '\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u044b',
            },
        ),
        migrations.AlterUniqueTogether(
            name='characteristictype',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='characteristic_type',
            field=models.ForeignKey(to='catalog.CharacteristicType'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='product',
            field=models.ForeignKey(verbose_name='Product', to='catalog.Product', help_text='Referenced product'),
        ),
        migrations.AlterUniqueTogether(
            name='characteristic',
            unique_together=set([('product', 'characteristic_type')]),
        ),
    ]
