from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
