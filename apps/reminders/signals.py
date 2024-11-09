# apps/reminders/signals.py

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MealReminder, ShoppingReminder

@receiver(post_save, sender=MealReminder)
def send_meal_reminder_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Meal Reminder',
            f"Don't forget to have your {instance.meal_time} at {instance.reminder_time}.",
            'no-reply@example.com',
            [instance.user.email],
            fail_silently=False,
        )

@receiver(post_save, sender=ShoppingReminder)
def send_shopping_reminder_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Shopping Reminder',
            f"Don't forget to buy: {instance.items}",
            'no-reply@example.com',
            [instance.user.email],
            fail_silently=False,
        )
