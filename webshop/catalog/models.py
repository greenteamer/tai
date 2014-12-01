# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.db import models
import decimal
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class CommonActiveManager(models.Manager):
    """Класс менеджер для фильтрации активных объектов"""
    def get_query_set(self):
        return super(CommonActiveManager, self).get_query_set().filter(is_active=True)


class Category(MPTTModel):
    """Класс для категорий товаров"""
    name = models.CharField(_(u'Name'), max_length=50, unique=True)
    slug = models.SlugField(_(u'Slug'), max_length=50, unique=True,
                            help_text=_(u'Slug for product url created from name.'))
    # "Чистые" ссылки для продуктов формирующиеся из названия
    description = models.TextField(_(u'Description'), blank=True)
    is_active = models.BooleanField(_(u'Active'), default=True)
    meta_keywords = models.CharField(_(u'Meta keywords'), max_length=255,
                                     help_text=_(u'Comma-delimited set of SEO keywords for meta tag'),blank=True)
    # Разделенные запятыми теги для SEO оптимизации
    meta_description = models.CharField(_(u'Meta description'), max_length=255,
                                        help_text=_(u'Content for description meta tags'), blank=True)
    created_at = models.DateTimeField(_(u'Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Updated at'), auto_now=True)
    parent = TreeForeignKey('self', verbose_name=_(u'Parent category'),
                            related_name='children', blank=True,
                            help_text=_(u'Parent-category for current category'), null=True)
    active = CommonActiveManager()

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        # return self.name
        return '%s%s' % ('--' * self.level, self.name)

    @permalink
    def get_absolute_url(self):
        """Генерация постоянных ссылок на категории"""
        return ('catalog_category', (), {'category_slug': self.slug})


class FeauturedProductManager(models.Manager):
    def get_query_set(self):
        return super(FeauturedProductManager, self).get_query_set().filter(is_featured=True)

class BestsellerProductManager(models.Manager):
    def get_query_set(self):
        return super(BestsellerProductManager, self).get_query_set().filter(is_bestseller=True)

class AquaProductManager(models.Manager):
    def get_query_set(self):
        return super(AquaProductManager, self).get_query_set().filter(is_aqua=True)

class NewProductManager(models.Manager):
    def get_query_set(self):
        return super(NewProductManager, self).get_query_set().filter(is_new=True)


class FeelName(models.Model):
    """Словарная таблица цветов"""
    name = models.CharField(_(u'Вкус'), max_length=255)
    # product = models.ForeignKey(Product, verbose_name=u'Брэнд', blank=True)

    class Meta:
        db_table = 'Feel_product'
        verbose_name_plural = _(u'Вкус')

    def __unicode__(self):
        return self.name


class BrandName(models.Model):
    """Словарная таблица цветов"""
    name = models.CharField(max_length=255, verbose_name=u'Название бренда')
    # product = models.ForeignKey(Product, verbose_name=u'Брэнд', blank=True)

    class Meta:
        db_table = 'brand_product'
        verbose_name_plural = _(u'Бренды')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    """Класс для товаров"""
    name = models.CharField(_(u'Name'), max_length=255, unique=True)
    slug = models.SlugField(_(u'Slug'), max_length=255, unique=True,
                            help_text=_(u'Unique value for product page URL, created from name.'))
    brand_name = models.ForeignKey(BrandName, verbose_name=u'Название бренда', blank=True, null=True)

    # price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Цена')
    # new_price = models.DecimalField(max_digits=9, decimal_places=2,
    #                                 blank=True, default=0.00, verbose_name=u'Новая цена')
    not_available = models.BooleanField(_(u'Нет в наличии'))
    is_bestseller = models.BooleanField(_(u'Лучшие продажи'), default=False) # Лучшие продажи
    is_aqua = models.BooleanField(verbose_name=u'Жидкость')
    is_new = models.BooleanField(verbose_name=u'Новинка')

    description = models.TextField(_(u'Description'),blank=True)
    meta_keywords = models.CharField(_(u'Meta keywords'), max_length=255,
                                     help_text=_(u'Comma-delimited set of SEO keywords for meta tag'), blank=True)
    meta_description = models.CharField(_(u'Meta description'), max_length=255,
                                        help_text=_(u'Content for description meta tag'),blank=True)
    created_at = models.DateTimeField(_(u'Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Updated at'), auto_now=True)
    categories = models.ForeignKey(Category, verbose_name=_(u'Categories'),
                                        help_text=_(u'Categories for product'))

    feel = models.ManyToManyField(FeelName, verbose_name=u'Вкус', blank=True, null=True)
    # volume = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Объем')
    # weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Вес')

    objects = models.Manager()

    bestseller = BestsellerProductManager()
    aqua = AquaProductManager()
    new = NewProductManager()


    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name_plural = _(u'Products')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        """Генерация постоянных ссылок на товары"""
        return ('catalog_product', (), {'product_slug': self.slug})

    @property
    def sale_price(self):

        # bool = False
        sale_atr = None
        atributes = ProductVolume.objects.filter(product=self)

        for atr in atributes:
            if atr.new_price != 0.00:
                sale_atr = atr
            else:
                sale_atr = ProductVolume.objects.get(product=self, default=True)
        return sale_atr

    def get_atributes(self):
        atribites = ProductVolume.objects.get(product=self, default=True)
        return atribites

    def get_image(self):
        image = ProductImage.objects.get(product=self, default=True)
        return image

    def is_not_available(self):
        return self.not_available==True


class ProductImage(models.Model):
    """Изображения продуктов"""
    image = models.FileField(_(u'Image'), upload_to='products/images/',
                             help_text='Product image')
    description = models.CharField(_(u'Description'), max_length=255, blank=True)
    product = models.ForeignKey(Product, verbose_name=_(u'Product'),
                                help_text=_(u'Referenced product'))
    default = models.BooleanField(_(u'Основное фото'), default=False)

    class Meta:
        db_table = 'product_images'
        verbose_name_plural = _(u'Изображения')

    @property
    def url(self):
        return self.image

    def __unicode__(self):
        return self.product.name


# модель для добавления основных свойств продукта
class ProductVolume(models.Model):
    volume = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Объем')
    weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Вес')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Цена')
    new_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    blank=True, default=0.00, verbose_name=u'Новая цена')

    default = models.BooleanField(_(u'Основной набор'), default=False)

    product = models.ForeignKey(Product, verbose_name=_(u'Product'), help_text=_(u'Referenced product'))

    class Meta:
        db_table = 'product_volume'
        verbose_name_plural = _(u'Основные атрибуты')

    def __unicode__(self):
        return '%s-%s' % (self.product.name, self.volume)


class GiftPrice(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название подарка')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Цена')
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(verbose_name=u'Фото подарка', upload_to='gifts/images/')
    weight = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Вес')

    class Meta:
        db_table = 'gift_price'
        ordering = ["-price"]
        verbose_name_plural = _(u'Подарки')

    def url(self):
        return self.image

    def __unicode__(self):
        return self.name


class CharacteristicType(models.Model):
    """Словарная таблица характеристик продуктов"""
    name = models.CharField(_(u'Name'), max_length=255)

    class Meta:
        db_table = 'characteristics_type'
        ordering = ['name']
        verbose_name_plural = _(u'Characteristics Types')
        unique_together = ('name',)

    def __unicode__(self):
        return self.name


class Characteristic(models.Model):
    """Характеристики продуктов"""
    characteristic_type = models.ForeignKey(CharacteristicType)
    value = models.CharField(_(u'Value'), max_length=255)
    product = models.ForeignKey(Product, verbose_name=_(u'Product'),
                                help_text=_(u'Referenced product'))

    class Meta:
        db_table = 'characteristics'
        ordering = ['characteristic_type', 'value']
        verbose_name_plural = _(u'Characteristics')
        # составной ключ, для избежания повторения одинковых характеристик у продукта
        unique_together = (('product', 'characteristic_type'),)


class Cupon(models.Model):
    name = models.CharField(verbose_name=u'Название купона', max_length=256)
    identifier = models.CharField(verbose_name=u'Идентификатор', max_length=256)
    percent = models.CharField(verbose_name=u'Процент скидки', max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Система купонов'