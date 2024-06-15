from rest_framework import serializers
from apps.users.services import retrieve_strip_session

from apps.users.models.payments import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class PaymentsStatusSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField()
    class Meta:
        model = Payments
        exclude = ['payment_link',]

    def get_payment_status(self, instance):
        return retrieve_strip_session(instance.payment_id)


