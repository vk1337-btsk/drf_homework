from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Users(AbstractUser):
    username = None

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

