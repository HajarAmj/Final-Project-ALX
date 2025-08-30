from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from recipes.views import RecipeViewSet, IngredientViewSet
from mealplans.views import MealPlanViewSet
from shopping.views import ShoppingListViewSet

router = routers.DefaultRouter()
router.register(r'api/recipes', RecipeViewSet, basename='recipes')
router.register(r'api/ingredients', IngredientViewSet, basename='ingredients')
router.register(r'api/meal-plans', MealPlanViewSet, basename='mealplans')
router.register(r'api/shopping-lists', ShoppingListViewSet, basename='shoppinglists')
# router.register(r'ingredients', IngredientViewSet)  # comment out until defined

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/auth/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

