from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Avatar
from django.utils.translation import gettext as _


class PaymentForm(forms.Form):
    num_card = forms.DecimalField(min_value=1000000000000000, max_digits=16)
