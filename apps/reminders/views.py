from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import MealReminder, ShoppingReminder
from .serializers import MealReminderSerializer, ShoppingReminderSerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_meal_reminder(request):
    """
    Create a new meal reminder for the authenticated user.
    - **meal_time**: The meal type (e.g., breakfast, lunch, dinner).
    - **reminder_time**: The time when the reminder should trigger.
    """
    serializer = MealReminderSerializer(data=request.data)
    if serializer.is_valid():
        reminder = serializer.save(user=request.user)
        return Response({"message": "Meal reminder created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def create_meal_reminder(request):
#     serializer = MealReminderSerializer(data=request.data)
#     if serializer.is_valid():
#         reminder = serializer.save(user=request.user)
#         return Response({"message": "Meal reminder created successfully."}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_shopping_reminder(request):
    serializer = ShoppingReminderSerializer(data=request.data)
    if serializer.is_valid():
        reminder = serializer.save(user=request.user)
        return Response({"message": "Shopping reminder created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_meal_reminder(request):
    meal_time = request.data.get('meal_time')
    reminder = MealReminder.objects.filter(user=request.user, meal_time=meal_time).first()
    if reminder:
        reminder.delete()
        return Response({"message": "Meal reminder deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    return Response({"message": "Reminder not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_shopping_reminder(request):
    reminder = ShoppingReminder.objects.filter(user=request.user).first()
    if reminder:
        reminder.delete()
        return Response({"message": "Shopping reminder deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    return Response({"message": "Reminder not found."}, status=status.HTTP_404_NOT_FOUND)
