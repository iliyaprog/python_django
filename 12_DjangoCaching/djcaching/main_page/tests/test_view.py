from django.test import TestCase
from django.urls import reverse


class FirstPageText(TestCase):

    def test_register_view(self):
        """Тест проверяет функцию login_view"""
        url = reverse('first_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_page.html')
