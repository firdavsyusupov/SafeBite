# apps/nutrition/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('nutrition-plan/generate/', views.generate_nutrition_plan, name='generate-nutrition-plan'),
]
