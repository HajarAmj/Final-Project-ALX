from django.db import models
from django.conf import settings

class ShoppingList(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shopping_lists')
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner})"

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, related_name='items', on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=40, blank=True)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ingredient_name} - {self.quantity} {self.unit}"
