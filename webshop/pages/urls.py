# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url
from django.contrib import admin

from webshop import settings

from webshop.pages.views import *

urlpatterns = patterns('webshop.pages.views',
    # url(r'^(?P<slug>[-_\w]+)/$', PageView.as_view(), name='page'),
    # url(r'^', PageList.as_view(), name='blog_posts'),
    url(r'^(?P<slug>[-_\w]+)/$', 'pageView',
        {'template_name':'pages/page.html'},
        name='page'),
)