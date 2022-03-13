from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from http import HTTPStatus


def home(request):
    return HttpResponse('Главная')
