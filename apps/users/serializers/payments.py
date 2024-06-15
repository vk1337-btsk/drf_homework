from rest_framework import serializers

from apps.users.models.payments import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

