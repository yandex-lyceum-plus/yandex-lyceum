from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def rating(request):
    return HttpResponse('rating page')
