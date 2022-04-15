from django.urls import path
from catalog import views


urlpatterns = [
    path('<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('', views.item_list, name='item_list'),
]
