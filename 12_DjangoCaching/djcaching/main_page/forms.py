from django import forms
from main_page.models import Product


class ProductForm(forms.Form):
    class Meta:
        model = Product
