# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls import patterns, url


urlpatterns = patterns('webshop.cart.views',
    url(r'^$', 'cart_view', {'template_name':'cart/cart.html'}, name='show_cart'),
)
