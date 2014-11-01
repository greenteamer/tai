# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from webshop.pages.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)
