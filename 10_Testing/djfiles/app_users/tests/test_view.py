from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class AppUserText(TestCase):

    def test_register_view(self):
        """Тест проверяет функцию register_view"""
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция register_view"""
        response = self.client.get('/app_users/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users.html')

    def test_edit_view(self):
        """Тест проверяет функцию edit_view"""
        url = reverse('edit_user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_page(self):
        """Тест проверяет шаблон и url на которые ссылается функция edit_view"""
        response = self.client.get('/app_users/edit_user')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_users.html')


User_Email = 'test@company.com'
Old_Password = 'test_password'

class RestorePasswordTest(TestCase):

    def test_restore_password(self):
        """Тест проверяет правильность работы восстановления пароля"""
        response = self.client.get('/app_users/password_recovery')
        self.assertEqual(response.status_code, 200)

    def test_restore_password_page(self):
        """Тест проверяет шаблон и url на которых происходит восстановление пароля"""
        response = self.client.get(reverse('recovery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_recovery.html')

    def test_post_password_recovery(self):
        """Отправляется тестовое письмо на тестовый email"""
        user = User.objects.create(username='test', email='User_Email')
        response = self.client.post(reverse('recovery'), {'email': User_Email})
        self.assertEqual(response.status_code, 200)
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        self.assertIn(User_Email, outbox[0].to)

    def test_if_password_was_challenge(self):
        """Тест проверяет, что у пользователя был изменен пароль"""
        user = User.objects.create(username='test', email=User_Email,)
        user.set_password(Old_Password)
        user.save()
        old_password_hash = user.password
        response = self.client.post(reverse('recovery'), {'email': User_Email})
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)


