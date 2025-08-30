from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Category

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
