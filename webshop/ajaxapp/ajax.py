#-*-coding:utf-8-*-
from django.utils import simplejson
from dajax.core import Dajax
from django.core import urlresolvers
from dajaxice.decorators import dajaxice_register
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from dajaxice.core import dajaxice_functions

from dajaxice.utils import deserialize_form
from webshop.catalog.forms import *
from django.core.mail import send_mail
from webshop.checkout.models import OrderOneClick
from webshop.checkout.forms import ContactForm, DeliveryForm
from webshop.checkout.models import Order, OrderItem
from webshop.checkout import checkout
from webshop.cart.cart import *
from webshop.cart import cart

@dajaxice_register
def order_form(request, form):
    dajax = Dajax()
    form = ContactForm(deserialize_form(form))
    dajax.add_css_class('#id_phone', 'error')
    if form.is_valid():
        dajax.remove_css_class('#order_form input', 'error')
        form.clean_phone()
        response = checkout.process(request)
        order_number = response.get('order_number', 0)
        order = response.get('order', 0)
        # получаем список заказынных товаров для передачи в письмо
        order_item = OrderItem.objects.filter(order_id=order.id)

        # test
        # dajax.assign('#id_email', 'value', errorText)

        items = ''
        for item in order_item:
            items = items + '%s \n' % item.name
        if order_number:
            request.session['order_number'] = order_number
            subject = u'7works заявка от %s' % request.POST['shipping_name']
            message = u'Заказ №: %s \n Имя: %s \n телефон: %s \n почта: %s \n id: %s \n Товары: \n %s' % (order_number, request.POST['shipping_name'], request.POST['phone'], request.POST['email'], order.id, items)
            send_mail(subject, message, 'teamer777@gmail.com', ['greenteamer@bk.ru'], fail_silently=False)

    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            errorText = ''
            if error == 'phone':
                errorText = u'формат терефона: 89237775522'
            elif error == 'email':
                errorText = u'формат email: example@gmail.com'
            dajax.add_css_class('#id_%s' % error, 'error')
            dajax.assign('#id_%s' % error, 'placeholder', errorText)

    return dajax.json()



@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = ProductOneClickForm(deserialize_form(form))
    # dajax.remove_css_class('#my_form .loading', 'hidden')
    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        # dajax.remove_css_class('#status', 'hidden')

        # result = u'Отправляем сообщение'
        # dajax.assign('#status', 'value', result)

        phone = form.cleaned_data.get('phone')
        product_name = form.cleaned_data.get('product_name')
        subject = u'Заявка в 1 клик'
        message = u'Телефон: %s \n Товар: %s' % (phone , product_name)
        send_mail(subject, message, 'teamer777@gmail.com', ['fish153.ru@gmail.com'], fail_silently=False)

        order = OrderOneClick(phone=phone , product_name=product_name)
        order.save()

        # dajax.remove_css_class('#status', 'hidden')
        # result = u'Сообщение отправлено'
        # dajax.assign('#status', 'value', result)
        dajax.remove_css_class('#message_show', 'hidden')
        # dajax.script('closemodal()')



        # dajax.redirect('/', delay=2000)
        # dajax.code('$(".close").click()')

    else:
        dajax.remove_css_class('#my_form input', 'error')
    #     dajax.remove_css_class('#status', 'hidden')
    #     result = u'Введите данные'
    #     dajax.assign('#status', 'value', result)
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')



    # dajax.add_css_class('div .loading', 'hidden')
    # dajax.alert("Form is_valid(), your phone is: %s" % form.cleaned_data.get('phone'))
    return dajax.json()


@dajaxice_register
def calc_delivery(request, form):
    dajax = Dajax()
    form = DeliveryForm(deserialize_form(form))
    if form.is_valid():

        # обновляем доставку и сохраняем в базу
        radio = form.cleaned_data.get('delivery')
        current_delivery = get_current_delivery(request)
        current_delivery.delivery_type = radio
        current_delivery.save()

        current_delivery = get_delivery(request)
        current_delivery.save()

        # обновляем инфу без преезагрузки
        dajax.assign('#type_ajax', 'innerHTML', '%s' % current_delivery.delivery_type )
        dajax.assign('#weight_ajax', 'innerHTML', '%s' % current_delivery.weight )
        dajax.assign('#price_ajax', 'innerHTML', '%s' % current_delivery.delivery_price )

    return dajax.json()

@dajaxice_register
def onload_cart(request):
    dajax = Dajax()

    # выключаем невозможные варианты
    # меняем способ доставки если не соответсвует требованиям
    current_delivery = get_delivery(request)

    # функция меняет данные на странице о текущем виде доставки
    def reset_data_delivery(data_type):
        dajax.assign('#type_ajax', 'innerHTML', '%s' % data_type )
        dajax.assign('#weight_ajax', 'innerHTML', '%s' % data_type )
        dajax.assign('#price_ajax', 'innerHTML', '%s' % data_type )

    def current_delivery_checked(request, type):
        delivery_label = {'SPSurface':'id_delivery_0', 'SPSAL':'id_delivery_1', 'SPA':'id_delivery_2', 'PS':'id_delivery_3', 'EMS':'id_delivery_4'}
        current_type = '#%s' % delivery_label['%s' % type]
        dajax.assign('%s' % current_type, 'checked', 'checked' )

    current_delivery_checked(request, current_delivery.delivery_type)

    if current_delivery.weight > 2000:
        dajax.assign('#id_delivery_0', 'disabled', 'disabled' )
        dajax.assign('#id_delivery_1', 'disabled', 'disabled' )
        dajax.assign('#id_delivery_2', 'disabled', 'disabled' )

        # меняем способ доставки если не соответсвует требованиям
        if current_delivery.delivery_type != 'PS' and current_delivery.delivery_type != 'EMS':
            current_delivery.delivery_type = 'PS'
            current_delivery.save()
            current_delivery = get_delivery(request)
            current_delivery.save()
            reset_data_delivery(current_delivery.delivery_type)

    if current_delivery.weight < 2000:
        dajax.assign('#id_delivery_3', 'disabled', 'disabled' )

        # меняем способ доставки если не соответсвует требованиям
        if current_delivery.delivery_type == 'PS':
            current_delivery.delivery_type = 'SPSurface'
            current_delivery.save()
            current_delivery = get_delivery(request)
            current_delivery.save()
            reset_data_delivery(current_delivery.delivery_type)

    for item in get_cart_items(request):
        if item.product.is_aqua:
            dajax.assign('#id_delivery_0', 'disabled', 'disabled' )
            dajax.assign('#id_delivery_1', 'disabled', 'disabled' )
            dajax.assign('#id_delivery_2', 'disabled', 'disabled' )
            dajax.assign('#id_delivery_3', 'disabled', 'disabled' )
            dajax.assign('#id_delivery_4', 'checked', 'checked' )

            # меняем способ доставки если не соответсвует требованиям
            if current_delivery.delivery_type != 'EMS':
                current_delivery.delivery_type = 'EMS'
                current_delivery.save()
                current_delivery = get_delivery(request)
                current_delivery.save()
                reset_data_delivery(current_delivery.delivery_type)


    return dajax.json()

