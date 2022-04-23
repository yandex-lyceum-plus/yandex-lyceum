from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Profile


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
