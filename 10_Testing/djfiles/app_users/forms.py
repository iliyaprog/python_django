from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия')
    email = forms.EmailField(max_length=40, required=True, help_text='Ваш email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class RestorePassword(forms.Form):
    email = forms.EmailField()
