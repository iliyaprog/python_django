from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from app_media.models import Feed
from django.contrib.auth.models import User


class FirstPageText(TestCase):

    def test_login_view(self):
        """Тест проверяет функцию login_view"""
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_login_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция login_view"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


    def test_get_detail_record(self):
        """тест проверяет функцию get_detail_record"""
        test_user = User.objects.create(username='test')
        test_user.save()
        test_object = Feed.objects.create(user=test_user, text='test')
        test_object.save()
        url = reverse('detail_record', args=(test_object.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_get_detail_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция get_detail_record"""
        test_user = User.objects.create(username='test')
        test_user.save()
        test_object = Feed.objects.create(user=test_user, text='test')
        test_object.save()
        response = self.client.get(f'/detail_record/{test_object.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_record.html')
