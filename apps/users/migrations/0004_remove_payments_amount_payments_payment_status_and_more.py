# Generated by Django 5.0.6 on 2024-06-15 22:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments_amount_payments_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='amount',
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_status',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Статус платежа'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id платежа'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
