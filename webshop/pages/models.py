#coding: utf-8
from django.db import models
from autoslug import AutoSlugField
from webshop.accounts.models import UserProfile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    name = models.CharField(verbose_name=u'Заголовок', max_length=100)
    slug = AutoSlugField(default='default', editable=True)
    text = RichTextField(verbose_name=u'Текст страницы', config_name='default')

    is_main = models.BooleanField(verbose_name=u'На главную')

    class Meta:
        verbose_name_plural = (u'Страницы')

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(verbose_name=u'Заголовок', max_length=100)
    slug = AutoSlugField(default='default', editable=True)
    text = models.TextField()

    menu_select = models.CharField(
        max_length=20,
        verbose_name=u'Выбор раздела',
        choices=(
            ('section1', 'Первый раздел'),
            ('section2', 'Второй раздел'),
            ('section3', 'Третий раздел'),
        ),
        default='section1',
    )

    class Meta:
        verbose_name_plural = (u'Блог автора')

    def __unicode__(self):
        return self.name

    def url(self):
        return '/blog/%s' % self.slug


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    review = models.TextField(verbose_name=u'Отзыв')


    def __unicode__(self):
        userName = UserProfile.objects.get(user=self.user)
        if userName.shipping_name:
            return (u'Отзыв: ') + userName.shipping_name
        else:
            return (u'Отзыв: ') + self.user.username


    class Meta:
        verbose_name_plural = (u'Отзывы пользователей')