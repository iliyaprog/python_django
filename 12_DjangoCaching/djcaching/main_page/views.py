from django.shortcuts import render
from django.utils.translation import gettext as _
from main_page.models import Product
from django.core.cache import cache


def first_page(request, *args, **kwargs):
    username = request.user.username
    products_cache_key = 'products:{}'.format(username)
    products = Product.objects.all()
    cache.get_or_set(products_cache_key, products, 1800)
    return render(request, 'main_page.html', {'products': products})
