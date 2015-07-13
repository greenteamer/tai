# -*- coding: utf-8 -*-
#!/usr/bin/env python
import decimal
import random

from django.shortcuts import get_object_or_404

from webshop.catalog.models import *
from webshop.checkout.models import Delivery
from webshop.cart.models import CartItem


CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    """
      Получение id корзины из cookies для пользователя,
      или установка новых cookies если не существуют
      _модификатор для видимости в пределах модуля
      """
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    """Генерация уникального id корзины который будет хранится в cookies"""
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters) - 1)]
    return cart_id

def get_cart_items(request):
    """Получение всех товаров для текущей корзины"""
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    """Добавление товара в корзину"""
    postdata = request.POST.copy()

    # Получаем чистое имя товара, возвращает пустую строку если нет
    product_slug = postdata.get('product_slug', '')

    # Получаем количество добавлеых товаров, возрат 1 если нет
    quantity = postdata.get('quantity', 1)

    # получаем набор атрибутов
    atr_value = postdata.get('atr_value', '')
    atributes = ProductVolume.objects.get(id=atr_value)

    # получаем вкус
    feel = postdata.get('feel', '')
    if feel == '':
        feel = None

    # Получаем товар, или возвращаем ошибку "не найден" если его не существует
    p = get_object_or_404(Product, slug=product_slug)

    # Получаем товары в корзине
    cart_products = get_cart_items(request)
    cupon = get_cupon(request)
    product_in_cart = False

    # Проверяем что продукт уже в корзине
    for cart_item in cart_products:
        if (cart_item.product.id == p.id) and ((cart_item.feel_id == feel) or ('%s' % cart_item.feel_id == feel)) and (cart_item.atributes == atributes):
            # Обновляем количество если найден
            cart_item.augment_quantity(quantity)
            product_in_cart = True

    if not product_in_cart:
        # Создаем и сохраняем новую корзину
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.cupon = cupon

        ci.atributes = atributes

        try:
            feelProduct = get_object_or_404(FeelName, id=feel)
        except Exception:
            feelProduct = None
        ci.feel = feelProduct


        ci.save()

def cart_distinct_item_count(request):
    """Возвращает общее количество товаров в корзине"""
    return get_cart_items(request).count()

def get_single_item(request, item_id):
    """Получаем конкретный товар в корзине"""
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))

def update_cart(request):
    """Обновляет количество отдельного товара"""
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
    #else:
    #TODO: добавить предупреждение
    #    remove_from_cart(request)

def update_cupon_cart(request):
    cart_products = get_cart_items(request)
    postdata = request.POST.copy()
    cupon_code ='%s' % postdata['cupon']
    try:
        cupon_true = Cupon.objects.get(identifier=cupon_code)
    except Exception:
        cupon_true = Cupon.objects.get(identifier='zero')
    for cart_item in cart_products:
        cart_item.cupon = cupon_true
        cart_item.save()

def get_cupon(request):
    cart_items = get_cart_items(request)
    cupon = Cupon.objects.get(identifier='zero')
    if cart_items:
        for item in cart_items:
            cupon = item.cupon
    return cupon

def remove_from_cart(request):
    """Удаляет выбранный товар из корзины"""
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()

def cart_subtotal(request):
    """Получение суммарной стоимости всех товаров"""
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += (cart_item.price - (cart_item.price * int(cart_item.cupon.percent) / 100)) * cart_item.quantity
    return cart_total

def cart_delivery_total(request):
    delivery = get_current_delivery(request)
    return delivery.delivery_price

def cart_total(request):
    total = cart_subtotal(request) + cart_delivery_total(request)
    return total

def cart_gift_add(request):
    """добавляем подарок"""
    gifts = GiftPrice.objects.all()
    cart_total = cart_subtotal(request)
    # result = GiftPrice()
    for gift in gifts:
        if gift.price < cart_total:

            result = gift

            try:
                result.image_url = GiftPrice.objects.get(product=gift, default=True).url
            except Exception:
                result.image_url = "/media/products/images/none.png"

            return result


def is_empty(request):
    """Если корзина пустая возвращаем True"""
    return cart_distinct_item_count(request) == 0

def empty_cart(request):
    """Очищает корзину покупателя"""
    user_cart = get_cart_items(request)
    user_cart.delete()






                                                    ### ДОСТАВКА ###
# подчсет доставки
# сохраняем доставку и возвращием во вьюху
def get_delivery(request):

    delivery = get_current_delivery(request)

    delivery.gift = cart_gift_add(request)
    weight = calculate_delivery_weight(request, delivery.gift)

    if delivery.delivery_type == '':
        if weight > 2000:
            delivery.delivery_type = 'PS'
        if weight < 2000:
            delivery.delivery_type = 'SPSurface'

    delivery.delivery_price = calculate_delivery_price(request, delivery)
    delivery.save()

    return delivery

# получаем текущую доставку или создаем новую
def get_current_delivery(request):
    try:
        delivery = Delivery.objects.get(cart_id_delivery=_cart_id(request))
    except Exception:
        delivery = Delivery()
        delivery.cart_id_delivery = '%s' % _cart_id(request)
    return delivery

# считаем вес доставки
def calculate_delivery_weight(request, gift):
    items = get_cart_items(request)
    delivery_weight = 0

    for item in items:
        delivery_weight += item.atributes.weight * item.quantity

    if gift:
        gift_weight = gift.weight
        delivery_weight = delivery_weight + gift_weight

    delivery_weight = delivery_weight

    return delivery_weight

# считаем стоимость доставки
def calculate_delivery_price(request, delivery):

    # КОНСТАНТЫ
    # EMS = { 0:1350, 250:1500, 500:1830, 1000:2160, 1500:2490, 2000:2820, 2500:3150, 3000:3480, 3500:3810, 4000:4140, 4500:4470, 5000:4800, 5500:5130, 6000:5460, 6500:5790, 7000:6120, 7500:6450, 8000:6780, 8500:7110, 9000:7440, 9500:7770, 10000:8100, 10500:8430, 11000:8760, 11500:9090, 12000:9420, 12500:9750, 13000:10080, 13500:10410, 14000:10740, 14500:11070, 15000:11400, 15500:11730, 16000:12060, 16500:12390, 17000:12720, 17500:13050, 18000:13380, 18500:13710, 19000:14040, 19500:1437, }
    # SPSurface = { 0:260, 200:360, 300:360, 400:360, 500:560, 600:560, 700:560, 800:560, 900:560, 1000:760,1100:760, 1200:760, 1300:760, 1400:760, 1500:960, 1600:960, 1700:960, 1800:960, 1900:96, }
    # SPSAL = { 0:180, 200:220, 300:270, 400:310, 500:360, 600:400, 700:450, 800:490, 900:540, 1000:580,1100:630, 1200:670, 1300:720, 1400:760, 1500:810, 1600:850, 1700:900, 1800:940, 1900:99, }
    # SPA = { 0:210, 200:270, 300:330, 400:400, 500:460, 600:520, 700:580, 800:650, 900:710, 1000:770, 1100:830, 1200:900, 1300:960, 1400:1020, 1500:1080, 1600:1150, 1700:1210, 1800:1270, 1900:133, }
    # PS = { 2000:1523, 3000:1680, 4000:1859, 5000:2027, 6000:2195, 7000:2363, 8000:2520, 9000:2699, 10000:2867, 11000:3030, 12000:3203, 13000:3371, 14000:3539, 15000:3707, 16000:3875, 17000:4043, 18000:4211, 19000:4379 }



    EMS = { 0:1980, 250:2200, 500:2680, 1000:3160, 1500:3640, 2000:4120, 2500:4600, 3000:5120, 3500:5480, 4000:5840, 4500:6200, 5000:6560, 5500:6920, 6000:7280, 6500:7640, 7000:8000, 7500:8360, 8000:8840, 8500:9160, 9000:9480, 9500:9800, 10000:10120, 10500:10440, 11000:10760, 11500:11080, 12000:11400, 12500:11720, 13000:12040, 13500:12360, 14000:12680, 14500:13000, 15000:13320, 15500:13640, 16000:13960, 16500:14280, 17000:14600, 17500:14920, 18000:15240, 18500:15560, 19000:15880, 19500:16200,}
    SPSurface = { 0:260, 200:360, 300:360, 400:360, 500:560, 600:560, 700:560, 800:560, 900:560, 1000:760,1100:760, 1200:760, 1300:760, 1400:760, 1500:960, 1600:960, 1700:960, 1800:960, 1900:960, }
    SPSAL = { 0:288, 200:360, 300:432, 400:504, 500:576, 600:648, 700:720, 800:792, 900:864, 1000:936, 1100:1008, 1200:1080, 1300:1152, 1400:1224, 1500:1296, 1600:1368, 1700:1440, 1800:1512, 1900:1584, }
    SPA = { 0:342, 200:442, 300:542, 400:642, 500:742, 600:842, 700:942, 800:1042, 900:1142, 1000:1242, 1100:1342, 1200:1442, 1300:1542, 1400:1642, 1500:1742, 1600:1842, 1700:1942, 1800:2042, 1900:2142, }
    PS = { 2000:2180, 3000:2420, 4000:2660, 5000:2900, 6000:3140, 7000:3380, 8000:3620, 9000:3860, 10000:4100, 11000:4340, 12000:4580, 13000:4820, 14000:5060, 15000:5300, 16000:5540, 17000:5780, 18000:6020, 19000:6260, }



    if delivery.delivery_type == 'EMS':
        delivery = look_at_price_delivery(request, delivery, EMS)

    if delivery.delivery_type == 'SPSurface':
        delivery = look_at_price_delivery(request, delivery, SPSurface)

    if delivery.delivery_type == 'SPSAL':
        delivery = look_at_price_delivery(request, delivery, SPSAL)

    if delivery.delivery_type == 'SPA':
        delivery = look_at_price_delivery(request, delivery, SPA)

    if delivery.delivery_type == 'PS':
        delivery = look_at_price_delivery(request, delivery, PS)

    return delivery.delivery_price

# выбираем стоимость доставки по прайсу
def look_at_price_delivery(request, delivery, type):

    delivery.weight = calculate_delivery_weight(request, delivery.gift )

    for key in sorted(type):
            if delivery.weight > key and delivery.weight < 20000:
                delivery.delivery_price = type[key]

    return delivery
