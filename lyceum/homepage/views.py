from django.shortcuts import render
from catalog.models import Item
from random import shuffle


def home(request):
    ids = list(Item.objects.filter(is_published=True).values_list('pk', flat=True))
    shuffle(ids)
    items = Item.objects.published_item_and_tags().filter(id__in=ids[:3])

    return render(request, 'homepage/home.html', {
        "items": items
    })
