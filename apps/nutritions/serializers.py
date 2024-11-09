from rest_framework import serializers
from .models import NutritionPlan

class NutritionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = ['daily_calories', 'meals']
