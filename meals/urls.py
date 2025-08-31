from django.urls import path
from .views import MealListCreateView, CategoryListCreateView

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list-create'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]
