from django.shortcuts import render


def item_list(request):
    return render(request, 'catalog/item_list.html')


def item_detail(request, pk):
    return render(request, 'catalog/item_detail.html', {"pk": pk})  # Простите меня пожалуйста ^-^
