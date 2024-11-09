from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import NutritionPlan
from .serializers import NutritionPlanSerializer
from apps.users.models import UserProfile
from rest_framework import permissions

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_nutrition_plan(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    
    # Примерная логика расчета калорий (можно использовать более сложный алгоритм)
    daily_calories = (profile.weight * 24)  # Простая формула для расчета калорий
    
    # Генерация плана питания
    meals = [
        {"meal": "Breakfast", "calories": daily_calories * 0.25},
        {"meal": "Lunch", "calories": daily_calories * 0.35},
        {"meal": "Dinner", "calories": daily_calories * 0.30},
        {"meal": "Snack", "calories": daily_calories * 0.10},
    ]

    nutrition_plan = NutritionPlan.objects.create(
        user=user,
        daily_calories=daily_calories,
        meals=meals
    )

    serializer = NutritionPlanSerializer(nutrition_plan)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
