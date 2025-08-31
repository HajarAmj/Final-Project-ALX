from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class ShoppingListItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    recipes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all(), required=False
    )
    recipe_details = RecipeSerializer(source="recipes", many=True, read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('id','user','title','recipes','recipes_details','mealplan','items','created_at')

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ('id','user','title','created_at','items')
        read_only_fields = ('user','created_at')
