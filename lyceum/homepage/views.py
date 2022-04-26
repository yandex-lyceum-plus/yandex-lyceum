from django.shortcuts import render
from catalog.models import Item
from django.views.generic import TemplateView
from random import shuffle


class Home(TemplateView):
    template_name = 'homepage/home.html'
    
    def get_context_data(self):
        ids = list(Item.objects.filter(is_published=True).values_list('pk', flat=True))
        shuffle(ids)
        return {'items': Item.objects.published_item_and_tags().filter(id__in=ids[:3])}
