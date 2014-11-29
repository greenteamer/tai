# -*- coding: utf-8 -*-
#!/usr/bin/env python
import decimal

from django.db import models

from webshop.catalog.models import Product, Cupon, FeelName, ProductVolume


class CartItem(models.Model):

    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False)

    atributes = models.ForeignKey(ProductVolume, unique=False)

    feel = models.ForeignKey(FeelName, unique=False, default=None, null=True)

    cupon = models.ForeignKey(Cupon, blank=True, null=True, default=2)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    @property
    def total(self):
        """Метод для подсчета суммы, цена товара * кол-во"""
        total = decimal.Decimal("0.00")
        total = self.quantity * self.price
        # total = "%d" % total
        return total

    @property
    def name(self):
        """Получение названия товара в корзине"""
        return self.product.name

    @property
    def price(self):
        """Получение цены товара в корзине"""
        set_price = decimal.Decimal("0.00")
        if self.atributes.new_price != 0.00:
            set_price = self.atributes.new_price
        else:
            set_price = self.atributes.price
        return set_price


    def get_absolute_url(self):
        """Получение абсолютной ссылки на товар"""
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        """Изменение количества товара в корзине"""
        if quantity.isdigit():
            self.quantity = self.quantity + int(quantity)
            self.save()
