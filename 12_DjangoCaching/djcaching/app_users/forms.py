from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Avatar
from django.utils.translation import gettext as _


class ExtendedRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AvatarForms(forms.Form):
    file = forms.ImageField()


class EditForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('Name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('Surname'))
    email = forms.EmailField(max_length=40, required=False, help_text='E-mail')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)