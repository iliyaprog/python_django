from django.urls import path

from app_products.views import DetailProduct, BuyProduct

urlpatterns = [
    path('detail_product/<int:product_id>', DetailProduct.as_view(), name='detail_product'),
    path('buy_product/<int:product_id>', BuyProduct.as_view(), name='buy_product')
]