from rest_framework import serializers
from .models import MealPlan, MealPlanAssignment
from recipes.serializers import RecipeSerializer

class MealPlanAssignmentSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=None)

    class Meta:
        model = MealPlanAssignment
        fields = ('id','plan','recipe','day','meal_type')
        read_only_fields = ('plan',)

class MealPlanSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField()

    class Meta:
        model = MealPlan
        fields = ('id','owner','name','start_date','end_date','created_at','assignments')
        read_only_fields = ('owner','created_at')

    def get_assignments(self, obj):
        return MealPlanAssignmentSerializer(obj.assignments.all(), many=True).data

class MealPlanCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ('id','name','start_date','end_date')
