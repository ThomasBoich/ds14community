# serializers.py
from rest_framework import serializers
from .models import CustomUser, Profile, PlayProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PlayProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayProfile
        fields = '__all__'