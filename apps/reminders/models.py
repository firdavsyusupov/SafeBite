# apps/reminders/models.py

from django.db import models
from django.contrib.auth import get_user_model

class MealReminder(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    meal_time = models.CharField(max_length=50)  # Завтрак, обед, ужин, перекус
    reminder_time = models.TimeField()  # Время напоминания
    is_active = models.BooleanField(default=True)  # Активно ли напоминание

    def __str__(self):
        return f"{self.user.username} - {self.meal_time} reminder at {self.reminder_time}"
    

class ShoppingReminder(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.TextField()  # Список продуктов
    reminder_time = models.DateTimeField()  # Время напоминания о покупках
    is_active = models.BooleanField(default=True)  # Активно ли напоминание

    def __str__(self):
        return f"{self.user.username} - Shopping reminder at {self.reminder_time}"
