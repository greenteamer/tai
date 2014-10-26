# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


from webshop.checkout.forms import CheckoutForm
from webshop.checkout.models import Order, OrderItem
from webshop.checkout import checkout
from webshop.cart import cart
from webshop.accounts import profile

from django.core.mail import send_mail, EmailMultiAlternatives
from webshop.checkout.forms import ContactForm
from django.shortcuts import render
from django.template.loader import render_to_string


# def checkout_view(request, template_name='checkout/checkout.html'):
#     """Представление для оформления заказа"""
#     if cart.is_empty(request):
#         cart_url = urlresolvers.reverse('show_cart')
#         return HttpResponseRedirect(cart_url)
#     if request.method == 'POST':
#         postdata = request.POST.copy()
#         form = CheckoutForm(postdata)
#         if form.is_valid():
#             response = checkout.process(request)
#             order_number = response.get('order_number', 0)
#             error_message = response.get('message', '')
#             if order_number:
#                 request.session['order_number'] = order_number
#                 receipt_url = urlresolvers.reverse('checkout_receipt')
#                 return HttpResponseRedirect(receipt_url)
#         else:
#             error_message = _(u'Correct the errors below')
#             if request.user.is_authenticated():
#                 user_profile = profile.retrieve(request)
#                 form = CheckoutForm(instance=user_profile)
#             else:
#                 form = CheckoutForm()
#     else:
#         form = CheckoutForm()
#     page_title = _(u'Checkout')
#     return render_to_response(template_name, locals(),
#                               context_instance=RequestContext(request))


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
            order_number = response.get('order_number', 0)
            order = response.get('order', 0)
            # получаем список заказынных товаров для передачи в письмо
            order_item = OrderItem.objects.filter(order_id=order.id)
            transaction = order.transaction_id
            items = ''
            for item in order_item:
                items = items + '%s \n' % item.name
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('checkout_receipt')

                # отправка письма админу
                subject = u'fish153.ru заявка от %s операция: %s' % (request.POST['shipping_name'], transaction)
                message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n почта: %s \n id: %s \n Товары: %s' % (order_number, request.POST['shipping_name'], request.POST['phone'], request.POST['email'], order.id, items)
                send_mail(subject, message, 'teamer777@gmail.com', ['fish153.ru@gmail.com'], fail_silently=False)

                # отправка html письма пользователю
                html_content = '<p>This is an <strong>important</strong> message.</p>'
                context_dict = {
                    'transaction': transaction,
                    'id': order.id,
                    'items': items,
                }
                message = render_to_string('checkout/email.html', context_dict)
                from_email = 'teamer777@gmail.com'
                to = '%s' % request.POST['email']
                msg = EmailMultiAlternatives(subject, message, from_email, [to])
                msg.content_subtype = "html"
                msg.send()

                return HttpResponseRedirect(receipt_url)
        else:

            # form = ContactForm(request.POST)
            return render(request, 'checkout/checkout.html', {
                'form': form,
                'error': form.errors,
            })
    else:
        form = ContactForm()
        # post = Post.objects.all()

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

    # return render(request, 'checkout/checkout.html', {
    #     'form': form,
    #     # 'posts': post,
    # })


def receipt_view(request, template_name='checkout/receipt.html'):
    """Представление отображающее сделанный заказ"""
    order_number = request.session.get('order_number', '')
    if order_number:
        # если в cookies есть номер заказа, выводим его содержимое
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        # иначе перенаправляем пользователя на страницу корзины
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
