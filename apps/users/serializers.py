from rest_framework import serializers
from apps.users.models import Users, Payments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'phone', 'city', 'is_staff']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    payments_list = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 'phone', 'city', 'is_staff', 'payments_list']