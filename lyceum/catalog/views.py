from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg, Count
from catalog.models import Item, Category
from rating.models import Rating
from django.views.generic import View


def item_list(request):
    categories = Category.objects.published_items_and_categories()

    return render(request, 'catalog/item_list.html', {
        'categories': categories
    })


class ItemDetail(View):
    def get(self, request, pk):
        item = get_object_or_404(
            Item.objects.published_item_and_tags(),
            pk=pk
        )

        user_star = '0'
        if request.user.is_authenticated:
            rate = Rating.objects.filter(
                item=item,
                user=request.user
            ).first()

            if rate:
                user_star = rate.star
        
        return render(request, 'catalog/item_detail.html', {
            'item': item,
            'variants': Rating.CHIOCES,
            'stars': item.ratings.exclude(star=0).aggregate(Avg('star'), Count('star')),
            'user_star': 5 - int(user_star),
        })

    def post(self, request, pk):
        item = get_object_or_404(
            Item.objects.published_item_and_tags(),
            pk=pk
        )
        if 'rate' in request.POST and request.POST['rate'].isdigit():
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
