from django.shortcuts import render


def user_list(request):
    return render(request, 'users/user_list.html')


def user_detail(request, pk):
    return render(request, 'users/user_detail.html')


def signup(request):
    return render(request, 'users/signup.html')


def profile(request):
    return render(request, 'users/profile.html')
