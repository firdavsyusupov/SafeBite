# apps/users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-profile/history/', views.user_profile_history, name='user-profile-history'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
