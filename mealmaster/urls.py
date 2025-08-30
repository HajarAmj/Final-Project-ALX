from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from recipes.views import RecipeViewSet, IngredientViewSet
from mealplans.views import MealPlanViewSet
from shopping.views import ShoppingListViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'api/recipes', RecipeViewSet, basename='recipes')
router.register(r'api/ingredients', IngredientViewSet, basename='ingredients')
router.register(r'api/meal-plans', MealPlanViewSet, basename='mealplans')
router.register(r'api/shopping-lists', ShoppingListViewSet, basename='shoppinglists')
# router.register(r'ingredients', IngredientViewSet)  # comment out until defined

urlpatterns = [
     path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/recipes/", include("recipes.urls")),
    path("api/mealplans/", include("mealplans.urls")),
    path("api/shopping/", include("shopping.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

