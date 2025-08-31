from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient, Category

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','name','default_unit')

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ('id','ingredient','quantity','unit')

class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Recipe
        fields = ('id','title','description','category','image','user','ingredients','created_at','updated_at')

class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id','title','description','category','image')
