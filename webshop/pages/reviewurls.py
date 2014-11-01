# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url

urlpatterns = patterns('webshop.pages.views',
    url(r'^$', 'review_form_view',
		{'template_name': 'pages/review.html' },
		name='review'),

)