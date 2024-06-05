import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.materials.models import Course, Lesson
from django.utils.translation import gettext as _


NULLABLE = {"blank": True, "null": True}


class Users(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default=uuid.uuid4)

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatar/', default='users/avatar/avatar_default.png',
                               verbose_name='Аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = '_us_users'
        ordering = ['email']


class Payments(models.Model):
    class PaymentMethodChoices(models.TextChoices):
        CASH = "Наличные", _("Наличные")
        CARD = "Карта", _("Карта")

    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_method = models.CharField(default=PaymentMethodChoices.CASH, choices=PaymentMethodChoices,
                                      verbose_name='Способ оплаты')

    def __str__(self):
        return (f"{self.user} | {self.payment_date} | {self.payment_amount} | {self.payment_method} | "
                f"{self.paid_course if self.paid_course else self.paid_lesson}")

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        db_table = '_us_payments'
        ordering = ['-payment_date',]
