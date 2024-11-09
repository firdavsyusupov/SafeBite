# apps/recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.get_recipes, name='get-recipes'),
]
