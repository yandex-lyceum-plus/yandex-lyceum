from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserForm
from users.models import Profile
from catalog.models import Item
import django.contrib.auth.views as admin_views


class Signup(View):
    def __init__(self):
        self.TEMPLATE = 'users/signup.html'
    
    def get(self, request):
        return render(request, self.TEMPLATE, {
            'form': UserRegistrationForm()
        })
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        return render(request, self.TEMPLATE, {
            'form': form
        })


class Login(View):
    def __init__(self):
        self.TEMPLATE = 'users/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        
        return render(request, self.TEMPLATE, {
            'form': UserLoginForm()
        })
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user and user.is_active:
                login(request, user)
                return redirect('profile')
            elif user:
                form.add_error(None, 'Аккаунт не активен')
            else:
                form.add_error(None, 'Пользователь не найден')
        return render(request, self.TEMPLATE, {
            'form': form
        })


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    TEMPLATE = 'users/profile.html'
    return render(request, TEMPLATE)


def profile(request):
    liked_items = Item.objects.user_liked_items(request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'items': liked_items,
        'user_form': user_form,
        'profile_form': profile_form
    }
    TEMPLATE = 'users/profile.html'
    return render(request, TEMPLATE, context=context)


def logout_page(request):
    logout(request)
    return redirect('home')


def user_detail(request, pk):
    user = get_object_or_404(User.objects.only(
        'email', 'first_name', 'last_name', 'profile__birthday'
    ).select_related('profile'), pk=pk)
    liked = Item.objects.user_liked_items(user)

    TEMPLATE = 'users/user_detail.html'
    return render(request, TEMPLATE, {
        'user': user,
        'items': liked,
    })


def user_list(request):
    TEMPLATE = 'users/user_list.html'
    users = User.objects.all().prefetch_related(
        Prefetch('profile', queryset=Profile.objects.all().only('birthday'))
    )
    return render(request, TEMPLATE, {
        'users': users
    })


class LoginView(admin_views.LoginView):
    template_name = 'users/login.html'


class PasswordChangeDoneView(admin_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class LogoutView(admin_views.LogoutView):
    template_name = 'users/logout.html'


class PasswordResetView(admin_views.PasswordResetView):
    template_name = 'users/password_reset.html'


class PasswordResetDoneView(admin_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(admin_views.PasswordResetConfirmView):
    template_name = 'users/reset.html'


class PasswordResetCompleteView(admin_views.PasswordResetCompleteView):
    template_name = 'users/reset_done.html'


class PasswordChangeView(admin_views.PasswordChangeView):
    template_name = 'users/password_change.html'
