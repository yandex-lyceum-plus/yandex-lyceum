from django.db import models
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from catalog.validators import validate_required_words, validate_words_count, validate_weight
from core.models import Published, Slug, Name
from rating.models import Rating


class CategoryManager(models.Manager):
    def published_items_and_categories(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch('items', queryset=Item.objects.published_item_and_tags())
        )


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True)


class ItemManager(models.Manager):
    def published_item_and_tags(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.published_tags()
            )
        )
    
    def user_liked_items(self, user):
        return self.filter(
            pk__in=Rating.objects.filter(
                user=user,
                star=5
            ).values_list('item_id')
        ).prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.published_tags()
            )
        ).only(
            'name',
            'text',
            'tags__name',
            'category_id',
        )

    def get_item(self, pk):
        return get_object_or_404(
            self.select_related('category').prefetch_related(
                Prefetch(
                    'tags',
                    queryset=Tag.objects.published_tags()
                ),
            ).only(
                'name',
                'text',
                'category__name',
                'tags__name'
            ),
            pk=pk,
            is_published=True
        )



class Item(Published):
    name = models.CharField(
        verbose_name='Название товара',
        max_length=150
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Минимум два слова. Обязательно должно содержаться слово превосходно или роскошно', validators=(validate_required_words, validate_words_count)
    )
    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        related_name='items'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='Category',
        related_name='items',
        on_delete=models.RESTRICT
    )
    
    objects = ItemManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(Slug, Published, Name):
    weight = models.PositiveSmallIntegerField(
        verbose_name='Вес',
        default=100,
        validators=(validate_weight, )
    )
    
    objects = CategoryManager()
    
    def __str__(self) -> str:
        return self.slug

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(Slug, Published, Name):
    objects = TagManager()

    def __str__(self) -> str:
        if self.name:
            return self.name
        return self.slug

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
