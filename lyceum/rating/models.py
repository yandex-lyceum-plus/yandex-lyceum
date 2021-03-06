from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Rating(models.Model):
    CHIOCES = (
        ('5', 'Любовь'),
        ('4', 'Обожание'),
        ('3', 'Нейтрально'),
        ('2', 'Неприязнь'),
        ('1', 'Ненависть'),
        ('0', 'Оценка отсутствует')
    )

    star = models.CharField(verbose_name='Оценка', max_length=1, choices=CHIOCES, default='0')
    item = models.ForeignKey(verbose_name='Товар', to='catalog.Item', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE, related_name='ratings')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = (UniqueConstraint(name='rating_unique', fields=('item', 'user')), )
    
    def __str__(self):
        return f'{self.item} | {self.user}'
