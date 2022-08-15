from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    USER = 'user'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'Пользователь'),
        (ADMIN, 'Администратор'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=9, choices=ROLES, default='user')
    image = models.ImageField()
