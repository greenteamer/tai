# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

from webshop.pages.models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)


class PageForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Page
        # exclude = ('slug',)

