from django.urls import path
from about import views


urlpatterns = [
    path('', views.Description.as_view(), name='description'),
]
