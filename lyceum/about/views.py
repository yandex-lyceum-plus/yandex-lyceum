from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def description(request):
    return HttpResponse('О проекте')
