from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.test import Client

from app_users.models import Bonus, ShoppingList


class AppUser(TestCase):

    def test_login_view(self):
        """Тест проверяет функцию login_view"""
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_view(self):
        """Тест проверяет функцию register_view"""
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_view(self):
        """Тест проверяет функцию logout_view"""
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_user_page(self):
    #     """Тест проверяет функцию user_page"""
    #     client = Client()
    #     bonus = Bonus.objects.create(user=client)
    #     bonus.save()
    #     shop_list = ShoppingList.objects.create(user=client)
    #     shop_list.save()
    #     url = reverse('user_page')
    #     response = client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'user_page.html')
    #
    # def test_upload_avatar_view(self):
    #     """Тест проверяет функцию upload_avatar_view"""
    #     url = reverse('upload_avatar')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'upload_avatar.html')

    def test_edit_view(self):
        """Тест проверяет функцию edit_view"""
        url = reverse('redactor_user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_users.html')