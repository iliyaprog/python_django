# from django.test import TestCase
# from django.urls import reverse
# from main_page.forms import ProductForm
# from main_page.models import Product
#
#
# class FormsMainPageTest(TestCase):
#
#     def test_request_created(self):
#         """Тест проверяет правильность работы формы ProductForm и модели Product"""
#         title = 'test'
#         description = 'test'
#         photo = 'test'
#         price = 10
#         data = {'title': title, 'description': description, 'photo': photo, 'price': price}
#         form = ProductForm(data=data)
#         if form.is_valid():
#             form.save()
#             assert Product.objects.filter(title=title).count == 1
