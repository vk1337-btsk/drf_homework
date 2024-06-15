
from rest_framework import serializers

from apps.users.models.users import Users
from apps.users.serializers.payments import PaymentsSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'is_superuser', 'is_staff', 'is_active']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'password']


class UserNotOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'first_name', 'is_active']


class UserDetailSerializer(serializers.ModelSerializer):
    payments_list = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = Users
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'is_superuser', 'is_staff', 'is_active',
                  'payments_list']
