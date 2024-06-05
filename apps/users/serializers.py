from rest_framework import serializers
from apps.users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'phone', 'city', 'is_staff']