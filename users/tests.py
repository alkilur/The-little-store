
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import EmailVerification, User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Richard', 'last_name': 'Miller',
            'username': 'alkilur', 'email': 'rmiller@gmail.com',
            'password1': '123456Pp', 'password2': '123456Pp',
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        response = self.client.post(self.path, self.data)
        # check creating of user
        username = self.data['username']
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # POST
        self.assertRedirects(response, reverse('users:login'))  # redirect
        self.assertTrue(User.objects.filter(username=username).exists())  # user created
        # check creation of EmailVeriification object
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
