from rest_framework import serializers
from .models import MealPlan, MealPlanAssignment
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe

class MealPlanAssignmentSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = MealPlanAssignment
        fields = ('id','plan','recipe','day','meal_type')
        read_only_fields = ('plan',)

class MealPlanSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="user.username")
    recipes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all()
    )
    recipe_details = RecipeSerializer(source="recipes", many=True, read_only=True)
   
    class Meta:
        model = MealPlan
        fields = ('id','user','title','start_date','end_date','created_at','assignments','description','recipes','recipes_details' )
        read_only_fields = ('user','created_at')

    def get_assignments(self, obj):
        return MealPlanAssignmentSerializer(obj.assignments.all(), many=True).data

class MealPlanCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ('id','title','start_date','end_date')
