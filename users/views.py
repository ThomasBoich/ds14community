from django.shortcuts import render

# Create your views here.



# views.py
from rest_framework import viewsets
from .models import CustomUser, Profile, PlayProfile
from .serializers import CustomUserSerializer, ProfileSerializer, PlayProfileSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PlayProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayProfile.objects.all()
    serializer_class = PlayProfileSerializer