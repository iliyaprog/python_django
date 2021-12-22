from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main_page.models import Product
from app_products.forms import PaymentForm
from app_users.models import Bonus, ShoppingList
from django.utils.translation import gettext_lazy as _


class DetailProduct(View):

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'detail_product.html', context={
            'product': product})


class BuyProduct(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        form = PaymentForm()
        return render(request, 'product_buy.html', context={
            'product': product, 'form': form})

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        bonus_obj = Bonus.objects.get(user=request.user)
        shop_obj = ShoppingList.objects.get(user=request.user)
        bonus = float(bonus_obj.bonus) + (float(product.price) * 0.05)
        if shop_obj.shop_list == ['']:
            shop = str(product.id)
        else:
            shop = shop_obj.shop_list + ',' + str(product.id)
        bonus_obj.delete()
        shop_obj.delete()
        ShoppingList.objects.create(user=request.user, shop_list=shop)
        Bonus.objects.create(user=request.user, bonus=bonus)

        return HttpResponse(_(f"Product:{product.title}, {product.price}$-paid for"))
