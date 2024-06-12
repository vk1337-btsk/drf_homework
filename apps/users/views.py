from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from apps.users.models import Users, Payments
from apps.users.permissions import IsOwnerOrReadOnly
from apps.users.serializers import UserSerializer, PaymentsSerializer, UserDetailSerializer, UserRegisterSerializer, \
    UserNotOwnerSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserDetailSerializer
        else:
            return UserNotOwnerSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = Users.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('payment_date',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
