from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget
from django.utils.translation import gettext_lazy as _


from app_users.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('Name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('Last_name'))
    date_of_birth = forms.DateField(required=False, help_text=_('Date of birth'),
                                    widget=SelectDateWidget(years=range(1910, 2020)))
    city = forms.CharField(max_length=30, required=False, help_text=_('City'))
    email = forms.EmailField(max_length=40, required=True, help_text=_('Your email'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    file = forms.FileField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()

