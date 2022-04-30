import imp
from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from django.forms.fields import BooleanField

class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if type(visible.field) != BooleanField:
                visible.field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(forms.ModelForm, BaseForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']


class UserForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'private_profile')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'private_profile': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
