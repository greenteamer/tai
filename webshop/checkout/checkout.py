# -*- coding: utf-8 -*-
#!/usr/bin/env python
#import urllib
import random
from django.core import urlresolvers

from webshop.cart import cart
from webshop.cart.cart import *
from webshop.checkout.models import Order, OrderItem
from webshop.catalog.models import Cupon
from webshop.checkout.forms import CheckoutForm, ContactForm
from webshop.accounts import profile

class TransactionResultType:
    """Возможные результаты транзакции"""
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'


def get_checkout_url(request):
    """Возвращает the URL для модуля оплаты"""
    return urlresolvers.reverse('checkout')

def process(request):

    transaction_id = random.randint(1, 999999)
    order = create_order(request, transaction_id)
    results = {'order_number': order.id, 'order': order}

    return results


def create_order(request, transaction_id):
    """
    Если POST запрос к платежной системе успешен, создаем новый заказ содержащий товары из корзины
    Сохраняем заказ с идентификатором транзации который вернет шлюз платежной системы
    В конце делаем очистку корзины
    """
    order = Order()
    checkout_form = ContactForm(request.POST, instance=order)
    checkout_form.shipping_address_1 = u'%s' % request.POST['shipping_address_1']
    order = checkout_form.save(commit=False)

    # присваиваем купон заказу по купону корзины
    cart_items = cart.get_cart_items(request)
    cupon = Cupon()
    for c in cart_items:
        cupon = c.cupon
    order.cupon = cupon

    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED

    delivery = get_current_delivery(request)
    order.delivery = delivery

    order.save()

    if order.pk:
        # Если заказ сохранен
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            # Создаем товар в заказе для каждого товара в корзине
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.feel = ci.feel
            oi.atributes = ci.atributes
            oi.save()
        # Очищаем корзину после оформления заказа
        cart.empty_cart(request)

        # Очищаем сессию cart_id
        request.session[CART_ID_SESSION_KEY] = ''

        # Сохраняем введенные данные для будующих заказов
        if request.user.is_authenticated():
            profile.set(request)

        # Сохраняем информацию о профиле пользователя
        if request.user.is_authenticated():
            profile.set(request)
    # Возвращаем объект - новый заказа
    return order
