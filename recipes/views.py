from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, Ingredient, RecipeIngredient, Category
from .serializers import RecipeSerializer, RecipeCreateUpdateSerializer, IngredientSerializer, RecipeIngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer    

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ('create','update','partial_update'):
            return RecipeCreateUpdateSerializer
        return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def image(self, request, pk=None):
        recipe = self.get_object()
        file = request.FILES.get('image')
        if not file:
            return Response({'detail':'No image provided.'}, status=status.HTTP_400_BAD_REQUEST)
        recipe.image = file
        recipe.save()
        return Response({'detail':'Image uploaded.'})

    @action(detail=True, methods=['get','post'])
    def ingredients(self, request, pk=None):
        recipe = self.get_object()
        if request.method == 'GET':
            items = recipe.recipe_ingredients.select_related('ingredient').all()
            serializer = RecipeIngredientSerializer(items, many=True)
            return Response(serializer.data)
        # POST -> add ingredient to the recipe
        payload = request.data
        ing_id = payload.get('ingredient_id')
        quantity = payload.get('quantity')
        unit = payload.get('unit','')
        try:
            ingredient = Ingredient.objects.get(id=ing_id)
        except Ingredient.DoesNotExist:
            return Response({'detail':'Ingredient not found'}, status=404)
        ri, created = RecipeIngredient.objects.update_or_create(
            recipe=recipe, ingredient=ingredient,
            defaults={'quantity':quantity or 0,'unit':unit}
        )
        serializer = RecipeIngredientSerializer(ri)
        return Response(serializer.data, status=201 if created else 200)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
