from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Content


class UserTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {
            "email": "test@example.com",
            "password": "Password123",
            "first_name": "Test",
            "last_name": "User",
            "phone": "1234567890",
            "pincode": "123456"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        url = reverse('login')
        user = User.objects.create_user(
            email="test@example.com", password="Password123")
        data = {
            "email": "test@example.com",
            "password": "Password123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ContentTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="author@example.com", password="Password123")
        self.client.login(email="author@example.com", password="Password123")

    def test_create_content(self):
        url = reverse('content-list-create')
        data = {
            "title": "Test Title",
            "body": "Test Body",
            "summary": "Test Summary",
            "document": "test.pdf",
            "categories": "test"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
