# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from webshop.settings import ADMIN_EMAIL
import decimal

# регистрация нового пользователя
import random
import string
from webshop.accounts.forms import UserProfileForm, MyRegistrationForm
from webshop.accounts.models import UserProfile, User
from django.contrib.auth import authenticate, login

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

    request.breadcrumbs(u'Данные получателя', request.path_info)

    if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        phone = request.POST['phone']

        if form.is_valid():

            form.clean_phone()

            """создание пользователя при оформлении заказа если не зарегистрирован"""
            #1 создать user
            #2 отправить письмо
            #3 создать User_profile
            if not request.user.is_authenticated():
                name , nu = request.POST['email'].split('@')[:2]
                try:
                    login_exist = User.objects.filter(username__icontains=name)
                    if login_exist:
                        name = '%s%s' % (name, login_exist.count())
                except Exception:
                    name = name

                new_user = User(username=name, email=request.POST['email'])
                password = User.objects.make_random_password()
                new_user.set_password(password)
                new_user.save()

                context_dict = {
                    'name': request.POST['shipping_name'],
                    'username': new_user.username,
                    'password': password,
                }

                subject = u'Регистрация на сайте www.polythai.ru'
                message = render_to_string('checkout/reg_email.html', context_dict)
                from_email = 'polythai@mail.ru'
                to = new_user.email
                msg = EmailMultiAlternatives(subject, message, from_email, [to])
                msg.content_subtype = "html"
                msg.send()

                user = authenticate(username=name, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        profile.set(request)


            """процесс создания заказа на основе того что было в корзине и на основе введенных данных"""
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

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def receipt_view(request, template_name='checkout/receipt.html'):
    """Представление отображающее сделанный заказ"""
    request.breadcrumbs(u'Подтверждение данных', request.path_info)

    order_id = request.session.get('order_id', '')
    if order_id:
        # если в cookies есть номер заказа, выводим его содержимое
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)

        delivery = order.delivery

        total = order.total
        if request.user.username == 'admin':
            total = 1

        if order.payment_method == 2:
            form = RobokassaForm(initial={
                   'OutSum': total,
                   'InvId': order.id,
               })
        else:

            """на данный момент следующий код не работает потому что отключена возможность выбора способа оплаты"""
            """отправка писем"""
            items = ''
            for item in order_items:
                items = items + '%s \n' % item.name
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


"""обрабатываем сигнал оплаты от платежной системы"""
def payment_received(sender, **kwargs):
    order = Order.objects.get(id=kwargs['InvId'])
    order.status = Order.PAID

    order.save()

    # обнуляем купон при успешном его использовании
    cupon_done = Cupon.objects.get(id=order.cupon.id)
    cupon_done.percent = '0'
    cupon_done.save()

    # отправляем письмо администратору
    order_items = OrderItem.objects.filter(order=order)
    items = ''
    for item in order_items:
        items = items + '%s %s (%s - %s) \n' % (item.name, item.get_feel(), item.atributes, item.atributes.getNewPrice())
    payment_method = u'Оплата произведена'
    subject = u'polythai.ru поступила оплата %s' % order.transaction_id
    message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n почта: %s \n id заказа: %s \n Товары: %s \n статус: %s \n <a href="%s">ссылка на заказ</a>' % (order.transaction_id, order.shipping_name, order.phone, order.email, order.id, items, payment_method, order.get_absolute_url())
    send_mail(subject, message, 'teamer777@gmail.com', [ADMIN_EMAIL], fail_silently=False)

    context_dict = {
            'name': order.shipping_name,
            'transaction': order.transaction_id,
            'id': order.id,
            'items': items,
            'total': order.total,
        }

    message = render_to_string('checkout/email.html', context_dict)
    from_email = 'polythai@mail.ru'
    to = '%s' % order.email
    msg = EmailMultiAlternatives(subject, message, from_email, [to])
    msg.content_subtype = "html"
    msg.send()

result_received.connect(payment_received)