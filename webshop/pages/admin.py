#coding: utf-8
from django.contrib import admin
from webshop.pages.models import *

class PageAdmin(admin.ModelAdmin):
    model = Page
    prepopulated_fields = {'slug':('name',)}

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Review)
admin.site.register(Blog, BlogAdmin)