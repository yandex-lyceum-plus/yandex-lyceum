from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg, Count
from catalog.models import Item, Category, Gallery
from rating.models import Rating
from django.views.generic import View, TemplateView


class ItemList(TemplateView):
    template_name = 'catalog/item_list.html'
    extra_context = {
        'categories': Category.objects.published_items_and_categories()
    }


class ItemDetail(View):
    def __init__(self) -> None:
        self.user_star = '0'
        self.template_name = 'catalog/item_detail.html'

    def get(self, request, pk):
        item = get_object_or_404(Item.objects.published_item_and_tags(), pk=pk)
        if request.user.is_authenticated:
            rate = Rating.objects.filter(item=item, user=request.user).first()
            if rate:
                self.user_star = rate.star
        return render(request, template_name=self.template_name, context={
            'item': item,
            'variants': Rating.CHIOCES,
            'stars': item.ratings.exclude(star=0).aggregate(Avg('star'), Count('star')),
            'user_star': 5 - int(self.user_star),
            'gallery': Gallery.objects.filter(item=item)
        })

    def post(self, request, pk):
        item = get_object_or_404(Item.objects.published_item_and_tags(),pk=pk)
        if request.POST.get('rate') and request.POST['rate'] in [choice[0] for choice in Rating.CHIOCES]:
            rate = request.POST['rate']
            if request.user.is_authenticated:
                Rating.objects.update_or_create(
                    item=item,
                    user=request.user,
                    defaults={
                        'star': rate
                    }
                )
        return redirect('item_detail', pk=pk)
