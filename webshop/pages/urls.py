# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url
from webshop.pages.views import *

# from webshop import settings

urlpatterns = patterns('',
    # (r'^$', ListView.object_list, all_models_dict),
    # url(r'^$', PostListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-_\w]+)/$', PageView.as_view(), name='page'),
)