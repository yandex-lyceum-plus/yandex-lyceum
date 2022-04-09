from django.db import models


class Published(models.Model):
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    class Meta:
        abstract = True


class Slug(models.Model):
    slug = models.SlugField(verbose_name='Идентификатор', unique=True, max_length=200)

    class Meta:
        abstract = True


class Name(models.Model):
    name = models.CharField(verbose_name='Название', max_length=25, blank=True, default='')

    class Meta:
        abstract = True
