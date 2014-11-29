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
from webshop.accounts import profile
from webshop.accounts.models import UserProfile
from webshop.pages.forms import ReviewForm

class PageView(DetailView):
    template_name = 'pages/page.html'
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context

class BlogList(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'blog_posts'
    template_name = 'pages/blog_list.html'


# class BlogListSectionOne(ListView):
#
#     queryset = Blog.objects.filter(menu_select='section1')
#     context_object_name = 'blog_section1'
#     template_name = 'pages/blog_list.html'

# выводим категорию блога
# def blogSection(request, section, template_name="pages/blog_list.html"):
#     blog_section = Blog.objects.filter(menu_select=section)
#     return render_to_response(template_name, locals(),context_instance=RequestContext(request))

# выводим статью блога
class BlogPost(DetailView):
    template_name = 'pages/blog.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogPost, self).get_context_data(**kwargs)
        return context

def review_form_view(request, template_name="pages/review.html"):
    try:
        current_userProfile = UserProfile.objects.get(user=request.user)
        reviews = Review.objects.all()
        if request.method == 'POST':
            postdata = request.POST.copy()
            form = ReviewForm(postdata)
            if form.is_valid():
                new_review = Review()
                new_review.review = postdata.get('review', '')
                new_review.user = request.user
                new_review.save()
                # new_review = form.save(commit=False)

                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
        else:
            user_profile = request.user
            form = ReviewForm(instance=user_profile)

    except:
        text = u'Вы не заполнили свой профиль'

    reviews = Review.objects.all()

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))