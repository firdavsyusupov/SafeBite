from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class NutritionPlan(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    daily_calories = models.IntegerField()
    meals = models.JSONField()  # Список с приемами пищи (завтрак, обед, ужин, перекус)

    def __str__(self):
        return f"Nutrition plan for {self.user.username}"
