# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from webshop.settings import ADMIN_EMAIL


from webshop.checkout.forms import CheckoutForm
from webshop.checkout.models import Order, OrderItem
from webshop.catalog.models import Cupon
from webshop.checkout import checkout
from webshop.cart import cart
from webshop.accounts import profile

from django.core.mail import send_mail, EmailMultiAlternatives
from webshop.checkout.forms import ContactForm, CheckoutForm
from django.shortcuts import render
from django.template.loader import render_to_string
from robokassa.signals import result_received


from robokassa.forms import RobokassaForm




def contact(request, template_name='checkout/checkout.html'):
    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        phone = request.POST['phone']

        if form.is_valid():

            form.clean_phone()
            response = checkout.process(request)

            order = response.get('order', 0)
            order_id = order.id

            if order_id:
                request.session['order_id'] = order_id
                receipt_url = urlresolvers.reverse('checkout_receipt')

                return HttpResponseRedirect(receipt_url)
        else:
            form = ContactForm(request.POST)
            return render(request, 'checkout/checkout.html', {
                'form': form,
                'error': form.errors,
            })
    else: #заполняем форму получателя если пользователь авторизирован
        if  request.user.is_authenticated():
            user_profile = profile.retrieve(request)
            form = ContactForm(instance=user_profile)
        else:
            form = ContactForm()

    # form = CheckoutForm()
    # form = ContactForm()

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


    # return render(request, 'checkout/checkout.html', {
    #     'form': form,
    #     # 'posts': post,
    # })


def receipt_view(request, template_name='checkout/receipt.html'):
    """Представление отображающее сделанный заказ"""
    # order_number = request.session.get('order_number', '')
    # if order_number:
    #     # если в cookies есть номер заказа, выводим его содержимое
    #     order = Order.objects.filter(id=order_number)[0]
    #     order_items = OrderItem.objects.filter(order=order)
    #     del request.session['order_number']
    # else:
    #     # иначе перенаправляем пользователя на страницу корзины
    #     cart_url = urlresolvers.reverse('show_cart')
    #     return HttpResponseRedirect(cart_url)
    # return render_to_response(template_name, locals(),
    #                           context_instance=RequestContext(request))

    order_id = request.session.get('order_id', '')
    if order_id:
        # если в cookies есть номер заказа, выводим его содержимое
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)

        delivery = order.delivery

        if order.payment_method == 2:
            form = RobokassaForm(initial={
                   'OutSum': order.total,
                   'InvId': order.id,
                   # 'Desc': order.shipping_name,
                   # 'Email': order.email,
                   # 'IncCurrLabel': '',
                   # 'Culture': 'ru'
               })
        else:

            """отправка писем"""
            items = ''
            for item in order_items:
                items = items + '%s вкус:%s \n' % (item.name, item.feel)
            if order.payment_method == 1:
                payment_method = u'Оплатить квитанцию'
            else:
                payment_method = u'Оплата онлайн'
            subject = u'polythai.ru заявка от %s' % order.shipping_name
            message = u'Номер транзакции №: %s \n Имя: %s \n телефон: %s \n почта: %s \n id заказа: %s \n Товары: %s \n %s \n Тип доставки: %s \n Вес доставки: %s \n Адрес: %s \n Стоимость доставки: %s \n Общая стоимость: %s' % (order.transaction_id, order.shipping_name, order.phone, order.email, order.id, items, payment_method, delivery.delivery_type, delivery.weight, order.shipping_address_1, delivery.delivery_price, order.total)
            send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

            context_dict = {
                    'transaction': order.transaction_id,
                    'id': order.id,
                    'items': items,
                    'total': order.total,
                    'payment_method': payment_method,
                }

            message = render_to_string('checkout/email.html', context_dict)
            from_email = 'teamer777@gmail.com'
            to = '%s' % order.email
            msg = EmailMultiAlternatives(subject, message, from_email, [to])
            msg.content_subtype = "html"
            msg.send()

            cupon_done = Cupon.objects.get(id=order.cupon.id)
            cupon_done.percent = '0'
            cupon_done.save()

            price_order = '%s' % order.total
            price_order = price_order.split(".")

            template_name = 'checkout/receipt_print.html'

        if request.POST == 'POST':
            del request.session['order_id']

    else:
        # иначе перенаправляем пользователя на страницу корзины
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


"""обрабатываем сигналы"""
def payment_received(sender, **kwargs):
    order = Order.objects.get(id=kwargs['InvId'])
    order.status = Order.PAID

    # order.paid_sum = kwargs['OutSum']
    order.save()

    # обнуляем купон при успешном его использовании
    cupon_done = Cupon.objects.get(id=order.cupon.id)
    cupon_done.percent = '0'
    cupon_done.save()

    # отправляем письмо администратору
    order_items = OrderItem.objects.filter(order=order)
    items = ''
    for item in order_items:
        items = items + '%s \n' % item.name
    payment_method = u'Оплата произведена'
    subject = u'polythai.ru заявка от %s' % order.shipping_name
    message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n почта: %s \n id заказа: %s \n Товары: %s \n %s' % (order.transaction_id, order.shipping_name, order.phone, order.email, order.id, items, payment_method)
    send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

    context_dict = {
            'transaction': order.transaction_id,
            'id': order.id,
            'items': items,
            'total': order.total,
            'payment_method': payment_method,
        }

    message = render_to_string('checkout/email.html', context_dict)
    from_email = 'teamer777@gmail.com'
    to = '%s' % order.email
    msg = EmailMultiAlternatives(subject, message, from_email, [to])
    msg.content_subtype = "html"
    msg.send()

result_received.connect(payment_received)