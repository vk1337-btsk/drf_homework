from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from apps.users.models import Users
from apps.users.serializers import UserSerializer, PaymentsSerializer, UserDetailSerializer
from rest_framework.filters import OrderingFilter
from apps.users.models import Users, Payments
from apps.users.serializers import UserSerializer, PaymentsSerializer, UserDetailSerializer
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('payment_date',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
