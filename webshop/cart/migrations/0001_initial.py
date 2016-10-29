# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_id', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('atributes', models.ForeignKey(to='catalog.ProductVolume')),
                ('cupon', models.ForeignKey(default=2, blank=True, to='catalog.Cupon', null=True)),
                ('feel', models.ForeignKey(default=None, to='catalog.FeelName', null=True)),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
            options={
                'ordering': ['date_added'],
                'db_table': 'cart_items',
            },
        ),
    ]
