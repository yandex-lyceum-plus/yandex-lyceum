from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch
from catalog.models import Category, Item, Tag


def item_list(request):
    items = Item.objects.published_item_and_tags()

    return render(request, 'catalog/item_list.html', {
        'items': items
    })


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.published_item_and_tags(), pk=pk)
    return render(request, 'catalog/item_detail.html', {
        'item': item
    })
