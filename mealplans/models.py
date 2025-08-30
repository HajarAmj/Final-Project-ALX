from django.db import models
from django.conf import settings
from recipes.models import Recipe

class MealPlan(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mealplans')
    name = models.CharField(max_length=200, default='My Meal Plan')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner})"

class MealPlanAssignment(models.Model):
    plan = models.ForeignKey(MealPlan, related_name='assignments', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    day = models.DateField()
    meal_type = models.CharField(max_length=50)

    class Meta:
        unique_together = ('plan','recipe','day','meal_type')

    def __str__(self):
        return f"{self.recipe.title} on {self.day} ({self.meal_type})"
