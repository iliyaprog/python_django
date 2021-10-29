from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    num_phone = forms.CharField(max_length=12, required=False, help_text='Номер телефона')
    city = forms.CharField(max_length=50, required=False, help_text='Город')
    data_of_birth = forms.DateField(required=True, help_text='Дата рождения')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')