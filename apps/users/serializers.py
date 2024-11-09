from rest_framework import serializers
from .models import UserProfile, UserProfileHistory

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'age', 'weight', 'height', 'gender', 'dietary_preference']

class UserProfileHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileHistory
        fields = ['date_of_birth', 'age', 'weight', 'height', 'gender', 'dietary_preference', 'updated_at']

# apps/users/serializers.py

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Отправляем email с кодом активации
        send_mail(
            'Welcome to the app',
            'Please verify your email address.',
            'no-reply@example.com',
            [user.email],
            fail_silently=False,
        )
        return user
    
# apps/users/serializers.py

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = get_user_model().objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        raise serializers.ValidationError('Invalid credentials')

