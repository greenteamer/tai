# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

import decimal
from webshop.settings import ADMIN_EMAIL
from django.core.mail import send_mail, EmailMultiAlternatives
from webshop.checkout.models import Order, OrderItem
from webshop.accounts.forms import UserProfileForm, MyRegistrationForm
from webshop.accounts import profile


@csrf_protect
def register_view(request, template_name="registration/register.html"):
    """Регистрация нового пользователя"""
    page_title = _(u'User Registration')
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = MyRegistrationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            # name="password1" т.к. два поля с подтверждением
            pw = postdata.get('password1', '')
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:

                # отправляем e-mail о регистрации нового пользователя
                subject = u'polythai.ru регистрация %s' % new_user.username
                message = u' Зарегистрирован новый пользователь %s' % (new_user.username)
                send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

                login(request, new_user)
                # Редирект на url с именем my_account
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = MyRegistrationForm()

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

@login_required
def my_account_view(request, template_name="registration/my_account.html"):
    """Страница аккаунта пользователя"""
    page_title = _(u'My Account')
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

@login_required
def order_details_view(request, order_id, template_name="registration/order_details.html"):
    """Информация о сделанном заказе"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = _(u'Order details for order #') + order_id
    order_items = OrderItem.objects.filter(order=order)
    total_sum_parse = "%s" % order.total
    total_sum_parse = total_sum_parse.split(".")
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

@login_required
def receipt_print_view(request, price, template_name="checkout/receipt_print.html"):
    price = price.split("-")
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

@login_required
def order_info_view(request, template_name="registration/order_info.html"):
    """Представление данных профиля"""
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = _(u'Edit Order Information')
    return render_to_response(template_name, locals(),
                                  context_instance=RequestContext(request))
