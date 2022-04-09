from django.shortcuts import get_object_or_404, render
from catalog.models import Item, Category


def item_list(request):
    categories = Category.objects.published_items_and_categories()

    return render(request, 'catalog/item_list.html', {
        'categories': categories
    })


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.published_item_and_tags(), pk=pk)
    return render(request, 'catalog/item_detail.html', {
        'item': item
    })
