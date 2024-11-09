# apps/reminders/apps.py

from django.apps import AppConfig

class RemindersConfig(AppConfig):
    name = 'apps.reminders'

    def ready(self):
        import apps.reminders.signals
