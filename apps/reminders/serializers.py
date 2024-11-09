# apps/reminders/serializers.py

from rest_framework import serializers
from .models import MealReminder, ShoppingReminder

class MealReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealReminder
        fields = ['meal_time', 'reminder_time', 'is_active']

class ShoppingReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingReminder
        fields = ['items', 'reminder_time', 'is_active']
