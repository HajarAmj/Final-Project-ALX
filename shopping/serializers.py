from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ('id','ingredient_name','quantity','unit','purchased')

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ('id','owner','name','created_at','items')
        read_only_fields = ('owner','created_at')
