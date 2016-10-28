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
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=255, verbose_name='Header')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('body', models.TextField(verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(null=True, verbose_name='Updated')),
                ('views', models.IntegerField(default=0, verbose_name='Views count', blank=True)),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'news',
                'verbose_name': 'Post',
                'verbose_name_plural': 'News',
                'get_latest_by': 'created',
            },
        ),
    ]
