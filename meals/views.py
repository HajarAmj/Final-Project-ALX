from rest_framework import generics, permissions
from .models import Meal, Category
from .serializers import MealSerializer, CategorySerializer

class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)
        category = self.request.query_params.get('category')
        ingredient = self.request.query_params.get('ingredient')
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if ingredient:
            queryset = queryset.filter(ingredients__icontains=ingredient)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

