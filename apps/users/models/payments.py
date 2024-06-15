from django.db import models
from django.utils.translation import gettext as _

from apps.materials.models import Course, Lesson
from apps.users.models.users import Users

NULLABLE = {"blank": True, "null": True}


class Payments(models.Model):
    class PaymentMethodChoices(models.TextChoices):
        CASH = "Наличные", _("Наличные")
        CARD = "Карта", _("Карта")

    user = models.ForeignKey(Users, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_method = models.CharField(default=PaymentMethodChoices.CASH, choices=PaymentMethodChoices,
                                      verbose_name='Способ оплаты')
    payment_id = models.CharField(max_length=255, **NULLABLE, verbose_name='id платежа')
    payment_link = models.URLField(max_length=400, **NULLABLE, verbose_name='Ссылка на оплату')
    payment_status = models.URLField(max_length=400, **NULLABLE, verbose_name='Статус платежа')

    def __str__(self):
        return (f"{self.user} | {self.payment_date} | {self.payment_amount} | {self.payment_method} | "
                f"{self.paid_course if self.paid_course else self.paid_lesson}")

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        db_table = '_us_payments'
        ordering = ['-payment_date', ]
