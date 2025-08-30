from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AccountsTests(APITestCase):
    def test_register_and_login(self):
        url = reverse("register")
        data = {"username": "testuser", "email": "test@example.com", "password": "testpass123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        login_url = reverse("login")
        login_data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(login_url, login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
