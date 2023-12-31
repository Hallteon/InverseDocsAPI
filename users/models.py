import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=256, verbose_name='Роль')
    role_type = models.CharField(max_length=100, verbose_name='Тип роли')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Username must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    firstname = models.CharField(max_length=256, blank=True, verbose_name='Имя')
    lastname = models.CharField(max_length=256, blank=True, verbose_name='Фамилия')
    surname = models.CharField(max_length=256, blank=True, verbose_name='Отчество')
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.CASCADE, related_name='users_role', verbose_name='Роль')
    password = models.CharField(max_length=256, verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



