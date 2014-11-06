# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from webshop.cart import cart
from webshop.checkout import checkout
from webshop.checkout.forms import ContactForm, DeliveryForm


@csrf_protect
def cart_view(request, template_name="cart/cart.html"):
    """Представление для отображения корзины"""
    page_title = _(u'Shopping cart')
    if request.method == 'POST':
        postdata = request.POST.copy()

        if postdata.has_key('remove'):
            cart.remove_from_cart(request)

        if postdata.has_key('update'):
            cart.update_cart(request)

        """отправляем request на пересчет корзины по купону"""
        if postdata.has_key('update_cupon'):
            cart.update_cupon_cart(request)


        if postdata.has_key('checkout'):
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)

    deliveryForm = DeliveryForm()

    # Получаем список всех товаров в корзине из cookies
    #cart_item_count = cart.cart_item_count(request)
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    cart_gift = cart.cart_gift_add(request)

    # доставка
    delivery = cart.get_delivery(request)
    # delivery.gift = cart_gift
    delivery.save()

    cart_total = cart.cart_total(request)
    # all_prices = cart.all_prices_for_delivery(request)
    # status = cart.status_delivery_radio(request)

    # test
    # test = ['hello', 'my', 'world']
    # test2 = ''.join(test)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
