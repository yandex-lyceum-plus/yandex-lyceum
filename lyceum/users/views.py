from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, TemplateView
from users.forms import UserRegistrationForm, ProfileForm, UserForm
from users.models import Profile
from catalog.models import Item
import django.contrib.auth.views as admin_views


class SignupPage(TemplateView):
    template_name = 'users/signup.html'
    extra_context = {'form': UserRegistrationForm()}
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        return redirect('login')


class ProfilePage(TemplateView):
    def __init__(self) -> None:
        self.template_name = 'users/profile.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        liked_items = Item.objects.user_liked_items(request.user)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'items': liked_items,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('profile')


class UserDetail(View):
    def __init__(self) -> None:
        self.template_name = 'users/user_detail.html'

    def get(self, request, pk):
        user = get_object_or_404(User.objects.only(
            'email', 'first_name', 'last_name', 'profile__birthday'
        ).select_related('profile'), pk=pk)
        liked = Item.objects.user_liked_items(user)
        extra_content = {
            'user': user,
            'items': liked,
        }
        return render(request, self.template_name, extra_content)


class UserList(TemplateView):
    template_name = 'users/user_list.html'
    extra_context = {
        'users': User.objects.all().prefetch_related(
            Prefetch('profile', queryset=Profile.objects.all().only('birthday'))
        )
    }


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
