# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_yasg.views import get_schema_view
from rest_framework_yasg import openapi

# Swagger view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Nutrition Plan API",
        default_version='v1',
        description="API for generating personalized nutrition plans, recipes, reminders, and user profiles.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@nutritionapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/nutrition/', include('apps.nutrition.urls')),
    path('api/recipes/', include('apps.recipes.urls')),
    # Swagger UI docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc UI docs
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
