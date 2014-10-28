#coding: utf-8
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Page(models.Model):
    name = models.CharField(verbose_name=u'Заголовок', max_length=100)
    slug = AutoSlugField(default='default', editable=True)
    text = RichTextField()

    menu_select = models.CharField(
        max_length=20,
        verbose_name=u'Выбор    меню',
        choices=(
            ('top_menu', 'верхнее меню'),
            ('useful', 'полезная информация'),
            ('footer_pages', 'информация в footer'),
        ),
        default='useful',
    )

    is_main = models.BooleanField(verbose_name=u'На главную')

    def __unicode__(self):
        return self.name

