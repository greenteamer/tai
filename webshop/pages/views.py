# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.views.generic import ListView, DetailView

from webshop.pages.models import *

class PageView(DetailView):
    template_name = 'pages/page.html'
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context

