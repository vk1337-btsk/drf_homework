from django.shortcuts import render
from rest_framework import viewsets
from apps.users.models import Users
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
