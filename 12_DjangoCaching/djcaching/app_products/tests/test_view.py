from django.test import TestCase
from django.urls import reverse
from main_page.models import Product
from django.test import Client



class AppProduct(TestCase):


    def test_get_detail_product(self):
        """Тест проверяет функцию get класса DetailProduct"""
        product = Product.objects.create(title='test',
                                         description='test',
                                         photo='test',
                                         price=10)
        product.save()
        response = self.client.get(f'/app_products/detail_product/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_product.html')

    def test_get_buy_product(self):
        """Тест проверяет функцию get класса BuyProduct"""
        product = Product.objects.create(title='test',
                                         description='test',
                                         photo='test',
                                         price=10)
        product.save()
        response = self.client.get(f'/app_products/buy_product/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_buy.html')

    # def test_post_buy_product(self):
    #     """Тест проверяет функцию post класса BuyProduct"""
    #     client = Client()
    #     product = Product.objects.create(title='test',
    #                                      description='test',
    #                                      photo='test',
    #                                      price=10)
    #     product.save()
    #     response = client.post(f"/app_products/buy_product/{product.id}",
    #                            {'username': 'test', 'first_name': 'test', 'last_name': 'test', 'email': 'test'})
    #     # response = self.client.post(f'/app_products/buy_product/{product.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'product_buy.html')