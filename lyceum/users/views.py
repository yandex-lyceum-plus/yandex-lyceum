from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def user_list(request):
    return HttpResponse('Список пользователей')


def user_detail(request, pk):
    return HttpResponse('Информация о пользователе')


def signup(request):
    return HttpResponse('Регистрация')


def profile(request):
    return HttpResponse('Мой профиль')
