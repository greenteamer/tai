# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'slider', verbose_name='\u0444\u043e\u0442\u043e \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430')),
                ('product', models.ForeignKey(verbose_name='\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442', to='catalog.Product')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b',
            },
        ),
    ]
