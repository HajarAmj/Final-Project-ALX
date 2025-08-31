from rest_framework import serializers
from .models import Meal, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class MealSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Meal
        fields = ('id', 'name', 'description', 'category', 'ingredients', 'user', 'created_at')
