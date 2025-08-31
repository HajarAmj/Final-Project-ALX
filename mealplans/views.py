from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import MealPlan, MealPlanAssignment
from .serializers import MealPlanSerializer, MealPlanCreateUpdateSerializer, MealPlanAssignmentSerializer
from shopping.models import ShoppingList, ShoppingListItem
from recipes.models import RecipeIngredient

class MealPlanViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('create','update','partial_update'):
            return MealPlanCreateUpdateSerializer
        return MealPlanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_assignment(self, request, pk=None):
        plan = self.get_object()
        payload = request.data
        recipe_id = payload.get('recipe_id')
        day = payload.get('day')
        meal_type = payload.get('meal_type','dinner')
        if not recipe_id or not day:
            return Response({'detail':'recipe_id and day required'}, status=status.HTTP_400_BAD_REQUEST)
        # create assignment
        data = {'plan': plan.id, 'recipe': recipe_id, 'day': day, 'meal_type': meal_type}
        serializer = MealPlanAssignmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=['post'])
    def generate_shopping_list(self, request, pk=None):
        plan = self.get_object()
        assignments = plan.assignments.select_related('recipe').all()
        agg = {}
        for a in assignments:
            recipe = a.recipe
            for ri in recipe.recipe_ingredients.all():
                key = (ri.ingredient.name, ri.unit)
                agg[key] = agg.get(key, 0) + (ri.quantity or 0)
        sl = ShoppingList.objects.create(user=request.user, name=f"Shopping for {plan.name}")
        for (ing_name, unit), qty in agg.items():
            ShoppingListItem.objects.create(shopping_list=sl, ingredient_name=ing_name, quantity=qty, unit=unit)
        return Response({'shopping_list_id': sl.id}, status=201)
