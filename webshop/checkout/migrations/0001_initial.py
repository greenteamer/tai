# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_type', models.CharField(default=b'', max_length=100, verbose_name='\u0441\u043f\u043e\u0441\u043e\u0431 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438', choices=[(b'SPSurface', b'Small Packet Surface'), (b'SPSAL', b'Small Packet SAL'), (b'SPA', b'Small Packet Air'), (b'PS', b'Parcel Surface'), (b'EMA', b'EMA')])),
                ('weight', models.IntegerField(default=0, verbose_name='\u0412\u0435\u0441')),
                ('delivery_price', models.DecimalField(max_digits=9, decimal_places=0)),
                ('cart_id_delivery', models.CharField(max_length=50)),
                ('gift', models.ForeignKey(verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u0430\u0440\u043e\u043a', blank=True, to='catalog.GiftPrice', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=50, verbose_name='\u0412\u0430\u0448 email')),
                ('phone', models.CharField(max_length=20, verbose_name='\u0412\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('shipping_name', models.CharField(max_length=240, verbose_name='\u0424\u0418\u041e \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f')),
                ('shipping_address_1', models.TextField(verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('shipping_city', models.CharField(max_length=200, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('shipping_address_2', models.TextField(verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441(\u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)', blank=True)),
                ('shipping_country', models.CharField(max_length=200, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430')),
                ('shipping_zip', models.CharField(max_length=10, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1, choices=[(1, '\u041f\u0440\u0438\u043d\u044f\u0442\u043e'), (2, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e'), (3, '\u041e\u043f\u043b\u0430\u0442\u0430 \u043a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u0435\u0439')])),
                ('payment_method', models.IntegerField(default=2, choices=[(1, '\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c \u043a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u044e'), (2, '\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c Viza, MasterCard, \u042f\u043d\u0434\u0435\u043a\u0441\u0414\u0435\u043d\u044c\u0433\u0438')])),
                ('ip_address', models.IPAddressField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=20)),
                ('cupon', models.ForeignKey(verbose_name='\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u044b\u0439 \u043a\u0443\u043f\u043e\u043d', blank=True, to='catalog.Cupon', null=True)),
                ('delivery', models.ForeignKey(to='checkout.Delivery', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('atributes', models.ForeignKey(to='catalog.ProductVolume')),
                ('feel', models.ForeignKey(default=None, to='catalog.FeelName', null=True)),
                ('order', models.ForeignKey(to='checkout.Order')),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOneClick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('phone', models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
            ],
            options={
                'ordering': ['product_name'],
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u044b',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b \u0432 1 \u043a\u043b\u0438\u043a',
            },
        ),
    ]
