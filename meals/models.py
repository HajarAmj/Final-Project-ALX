from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Meal(models.Model):
    class Meal(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meals")
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
        ingredients = models.TextField(help_text="Comma-separated ingredients")
        created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

