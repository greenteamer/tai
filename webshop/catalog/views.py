# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from webshop.cart import cart
from webshop.catalog.forms import ProductAddToCartForm
from webshop.catalog.models import *
from webshop.news.models import News
from webshop.pages.models import Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# testing
# import time
# reps = 2
# repslist = range(reps)


# # таймер вычисления скорости выполнения функции
# def timer(func, *pargs, **kargs):
#     start = time.clock()
#     for i in repslist:
#         ret = func(*pargs, **kargs)
#     elapsed = time.clock() - start
#     return (elapsed, ret)


# def my_test():
#     c = Category.objects.get(slug='dlya-tela')
#     loop_category = Category.objects.filter(tree_id=c.tree_id)
#     products = []
#     for category in loop_category:
#         products_subcategory = category.product_set.all()
#         for product in products_subcategory:
#             if product in products:
#                 continue
#             products.append(product)
#
#
# def my_test2():
#     c = Category.objects.get(slug='dlya-tela')
#     loop_category = Category.objects.filter(tree_id=c.tree_id)
#     products = set()
#     for cat in loop_category:
#         products_subcategory = set(cat.product_set.all())
#         products = products | products_subcategory
#
#
# def my_test3():
#     c = Category.objects.get(slug='dlya-tela')
#     products = set()
#     loop_category = map(
#         lambda x: set(x.product_set.all()),
#         list(Category.objects.filter(tree_id=c.tree_id)))

#     for p_set in loop_category:
#         products = products | p_set


def index_view(request, template_name="catalog/index.html"):
    """Представление главной страницы"""
    page_title = u'Интернет магазин'
    news = News.objects.all()[:5]
    try:
        frontpage = Page.objects.get(is_main='True')
    except Exception:
        frontpage = Page.objects.get(slug="404")
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


# функция фильтрации повторяющихся позиций
def sortAndUniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    output.sort()
    return output


def category_view(
        request, category_slug, template_name="catalog/category.html"):
    """для теста"""
    # for test in (my_test, my_test2, my_test3, ):
    #     elapsed, result = timer(test)
    #     print ('-' * 33)
    #     print ('%-9s: %.5f' % (test.__name__, elapsed))
    # print '--ok--'
    """Представление для просмотра конкретной категории"""
    c = get_object_or_404(Category.active, slug=category_slug)
    if c.level == 0:
        request.breadcrumbs('%s' % c.name, request.path_info)
        loop_category = Category.objects.filter(tree_id=c.tree_id)
        products = set()
        for cat in loop_category:
            products_subcategory = set(cat.product_set.all())
            products = products | products_subcategory
    else:
        products = c.product_set.all()
        # products = sortAndUniq(products)
        parent_cat = Category.objects.get(id=c.parent.id)
        parent_url = parent_cat.get_absolute_url()
        request.breadcrumbs([
            ('%s' % parent_cat.name, parent_url),
            ('%s' % c.name, request.path_info)
        ])

    for p in products:
        try:
            p.image_url = ProductImage.objects.get(product=p, default=True).url
        except Exception:
            p.image_url = "/media/products/images/none.png"
    products = sorted(products, key=lambda x: x.id, reverse=True)

    paginator = Paginator(products, 30)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def sale_view(request, template_name="", type=""):
    """Представление для просмотра скидок"""
    if type == 'sale':
        request.breadcrumbs(u'Скидки', request.path_info)
        page_name = 'Скидки - горячая цена'
        sale_arts = ProductVolume.objects.exclude(new_price=0.00)
        products = []
        for p in sale_arts:
            prod = Product.objects.get(id=p.product_id)
            products.append(prod)
        products = list(set(products))  # удаляем повторы

    else:
        request.breadcrumbs(u'Новинки', request.path_info)
        page_name = 'Новинки!'
        products = Product.objects.filter(is_new=True)
    for p in products:
        try:
            p.image_url = ProductImage.objects.get(product=p, default=True).url
        except Exception:
            p.image_url = "/media/products/images/none.png"
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def liderView(request, template_name="catalog/lider.html"):
    liders = Product.objects.filter(is_bestseller='True')
    for p in liders:
        try:
            p.image_url = ProductImage.objects.get(product=p, default=True).url
        except Exception:
            p.image_url = "/media/products/images/none.png"
    return render_to_response(
        template_name, locals(), context_instance=RequestContext(request))


@csrf_protect
def product_view(request, product_slug, template_name="catalog/product.html"):
    """Представление для просмотра конкретного продукта"""
    p = get_object_or_404(Product, slug=product_slug)
    cat = p.categories.all()
    c = get_object_or_404(Category, id=cat[0].id)
    if c.level == 0:
        request.breadcrumbs([
            ('%s' % c.name, request.path_info),
            ('%s' % p.name, request.path_info)
        ])

    else:
        parent_cat = Category.objects.get(id=c.parent.id)
        parent_url = parent_cat.get_absolute_url()
        request.breadcrumbs([
            ('%s' % parent_cat.name, parent_url),
            ('%s' % c.name, c.get_absolute_url()),
            ('%s' % p.name, request.path_info)
        ])

    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    try:
        """достаем все фотки + дефлтную"""
        product_image = ProductImage.objects.get(product=p, default=True)
        images = ProductImage.objects.filter(product=p)

    except Exception:
        print "Image for product #%s not found" % p.id
    characteristics = Characteristic.objects.filter(product=p)
    # достаем основные атрибуты

    try:
        atrs_default = ProductVolume.objects.get(product=p, default=True)
        atrs = ProductVolume.objects.filter(product=p)

    except Exception:
        print u'Основные атрибуты продукта %s не найдены' % p.name

    if request.method == 'POST':
        """Проверка HTTP метода
        Добавление в корзину, создаем связанную форму"""
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)

        if form.is_valid():
            """Добавляем в корзину и делаем перенаправление на
            страницу с корзиной"""
            cart.add_to_cart(request)
            # Если cookies работают, читаем их
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect('/product/%s' % product_slug)

        else:
            form = ProductAddToCartForm(request, postdata)
            error = form.errors
            return render_to_response(
                template_name, locals(),
                context_instance=RequestContext(request))

    else:
        """Если запрос GET, создаем не привязанную форму.
        request передаем в kwarg"""
        form = ProductAddToCartForm(request=request, label_suffix=':')

    """Присваиваем значению скрытого поля чистое имя продукта"""
    form.fields['product_slug'].widget.attrs['value'] = product_slug

    """Устанавливаем тестовые cookies при первом GET запросе"""
    request.session.set_test_cookie()
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
