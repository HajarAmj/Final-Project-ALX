from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from recipes.models import Recipe
from .models import ShoppingList

class ShoppingListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.client.login(username="tester", password="pass123")
        self.recipe = Recipe.objects.create(
            user=self.user,
            title="Salad",
            description="Fresh salad",
            ingredients="lettuce, tomato, cucumber",
            instructions="Mix all ingredients",
        )

    def test_create_shopping_list(self):
        url = reverse("shoppinglist-list")
        data = {
            "title": "Weekly Groceries",
            "recipes": [self.recipe.id],
            "items": "lettuce, tomato, cucumber",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShoppingList.objects.count(), 1)
        self.assertEqual(ShoppingList.objects.get().title, "Weekly Groceries")
