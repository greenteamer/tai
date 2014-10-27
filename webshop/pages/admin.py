#coding: utf-8
from django.contrib import admin
from webshop.pages.models import *

class PageAdmin(admin.ModelAdmin):
    model = Page
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page, PageAdmin)