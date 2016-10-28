# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439',
            },
        ),
    ]
