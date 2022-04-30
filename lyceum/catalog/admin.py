from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from catalog.models import Item, Category, Tag, Gallery
from catalog.templatetags.catalog_extras import render_markdown
from markitup.widgets import AdminMarkItUpWidget


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def get_text(self, object):
        return mark_safe(render_markdown(object.text))

    list_display = ('name', 'is_published', 'get_text', 'img_tmb',)
    list_display_links = ('name',)
    list_editable = ('is_published', )
    filter_horizontal = ('tags', )
    get_text.short_description = 'Текст'
    formfield_overrides = {
        models.TextField: {
            'widget': AdminMarkItUpWidget
        }
    }


@admin.register(Tag)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'is_published')
    list_display_links = ('slug',)
    list_editable = ('is_published', )


@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'weight', 'is_published')
    list_display_links = ('slug',)
    list_editable = ('is_published',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'item_image')
    list_display_links = ('item',)