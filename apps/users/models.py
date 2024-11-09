from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    dietary_preference = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

from django.utils import timezone

class UserProfileHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    dietary_preference = models.CharField(max_length=50, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Profile history for {self.user.username} at {self.updated_at}'