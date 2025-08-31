from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Recipe

class RecipeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.client.login(username="tester", password="pass123")

    def test_create_recipe(self):
        url = reverse("recipe-list")
        data = {
            "title": "Pasta",
            "description": "Delicious pasta with sauce",
            "ingredients": "pasta, tomato, salt",
            "instructions": "Boil pasta, add sauce",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.get().title, "Pasta")
