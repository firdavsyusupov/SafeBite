from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    calories = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
