from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from recipes.views import RecipeViewSet, IngredientViewSet
from mealplans.views import MealPlanViewSet
from shopping.views import ShoppingListViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'api/recipes', RecipeViewSet, basename='recipes')
router.register(r'api/ingredients', IngredientViewSet, basename='ingredients')
router.register(r'api/meal-plans', MealPlanViewSet, basename='mealplans')
router.register(r'api/shopping-lists', ShoppingListViewSet, basename='shoppinglists')
# router.register(r'ingredients', IngredientViewSet)  # comment out until defined

schema_view = get_schema_view(
    openapi.Info(
        title="MealMaster API",
        default_version="v1",
        description="API documentation for MealMaster project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@mealmaster.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/recipes/", include("recipes.urls")),
    path("api/mealplans/", include("mealplans.urls")),
    path("api/shopping/", include("shopping.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",

    # Local apps
    "accounts",
    "recipes",
    "mealplans",
    "shopping",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # enable CORS for frontend
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
