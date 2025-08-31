from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from recipes.models import Recipe
from .models import MealPlan
import datetime

class MealPlanTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.client.login(username="tester", password="pass123")
        self.recipe = Recipe.objects.create(
            user=self.user,
            title="Pasta",
            description="Delicious pasta",
            ingredients="pasta, tomato",
            instructions="Boil and mix",
        )

    def test_create_mealplan(self):
        url = reverse("mealplan-list")
        data = {
            "title": "Weekly Plan",
            "description": "Plan for the week",
            "recipes": [self.recipe.id],
            "start_date": datetime.date.today(),
            "end_date": datetime.date.today() + datetime.timedelta(days=7),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MealPlan.objects.count(), 1)
        self.assertEqual(MealPlan.objects.get().title, "Weekly Plan")
