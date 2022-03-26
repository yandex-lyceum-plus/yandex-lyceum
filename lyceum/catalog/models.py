from django.contrib.auth.models import User
from django.db import models

from catalog.validators import validate_required_words, validate_words_count
from core.models import Published, Slug


class Item(Published):
    name = models.CharField(max_length=150)
    text = models.TextField(verbose_name='Текст', help_text='Минимум два слова. Обязательно должно содержаться слово превосходно или роскошно', validators=(validate_required_words, validate_words_count))
    tags = models.ManyToManyField(verbose_name='Теги', to='Tag', related_name='items')
    category = models.ForeignKey(verbose_name='Категория', to='Category', related_name='items', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(Slug, Published):
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', default=100)

    def __str__(self) -> str:
        return self.slug

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(Slug, Published):
    def __str__(self) -> str:
        return self.slug

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'