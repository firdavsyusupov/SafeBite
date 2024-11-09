# apps/reminders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('meal/', views.create_meal_reminder, name='create-meal-reminder'),
    path('shopping/', views.create_shopping_reminder, name='create-shopping-reminder'),
    path('meal/delete/', views.delete_meal_reminder, name='delete-meal-reminder'),
    path('shopping/delete/', views.delete_shopping_reminder, name='delete-shopping-reminder'),
]
