from django.contrib.auth.models import User, Group, Permission
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.test import Client, RequestFactory
from first_page.views import login_view
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from unittest import mock

from app_media.models import Feed
from app_media.views import upload_records, upload_files


class AppMediaTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_upload_file(self):
        """Тест проверяет функцию upload_file"""
        url = reverse('upload_file')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_upload_file_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция upload_file"""
        response = self.client.get('/app_media/upload_file')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload_file.html')

    def test_model_form_upload(self):
        """Тест проверяет функцию model_form_upload"""
        url = reverse('model_form_upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_model_form_upload_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция model_form_upload"""
        response = self.client.get('/app_media/model_form_upload')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_form_upload.html')

    def test_upload_files_no_authenticate(self):
        """Тест проверяет функцию upload_files на доступ не аутентифицированного пользователя"""
        url = reverse('upload_files')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_upload_files_authenticate(self):
        """Тест проверяет функцию upload_files на доступ аутентифицированного пользователя"""
        test_user = User.objects.create(username='test', password='test')
        content_type = ContentType.objects.get_for_model(Feed)
        permission = Permission.objects.get(
            codename='add_feed',
            content_type=content_type,
        )
        test_user.user_permissions.add(permission)
        factory = RequestFactory()
        requests = factory.get('')
        requests.user = test_user
        response = upload_files(requests)
        print(self)
        self.assertEqual(response.status_code, 200)

    def test_upload_records_no_authenticate(self):
        """Тест проверяет функцию upload_records на доступ не аутентифицированного пользователя"""
        url = reverse('upload_records')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_upload_records_authenticate(self):
        """Тест проверяет функцию upload_records на доступ аутентифицированного пользователя"""
        test_user = User.objects.create(username='test', password='test')
        content_type = ContentType.objects.get_for_model(Feed)
        permission = Permission.objects.get(
            codename='add_feed',
            content_type=content_type,
        )
        test_user.user_permissions.add(permission)
        factory = RequestFactory()
        requests = factory.get('')
        requests.user = test_user
        response = upload_records(requests)
        self.assertEqual(response.status_code, 200)


