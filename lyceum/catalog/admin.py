from django.contrib import admin
from catalog.models import Item, Category, Tag, Gallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text', 'img_tmb',)
    list_display_links = ('name', 'text',)
    list_editable = ('is_published', )
    filter_horizontal = ('tags', )


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