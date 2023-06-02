from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from .buldings import *
from admin_panel.utilities import get_timestamp_path


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=19, verbose_name='Номер телефона',
                             validators=[
                                 validators.MaxLengthValidator(19),
                                 validators.MinLengthValidator(19),
                                 validators.ProhibitNullCharactersValidator(),
                                 validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                           message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                             ]
                             )
    STATUS_CHOICE = (
        ('new', 'Новый'),
        ('active', 'Активен'),
        ('disabled', 'Отключен'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='new', verbose_name='Статус')

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'


class HouseUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICE = (
        ('director', 'Директор'),
        ('manager', 'Управляющий'),
        ('accountant', 'Бухгалтер'),
        ('electrician', 'Электрик'),
        ('plumber', 'Сантехник'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICE, default='director', verbose_name='Роль')

    class Meta:
        db_table = 'houseuser'


class FlatOwner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, default='', blank=True)
    viber = models.CharField(verbose_name='Viber', max_length=100, default='', blank=True)
    telegram = models.CharField(verbose_name='Telegram', max_length=100, default='', blank=True)
    bio = models.TextField(verbose_name='О владельце (заметки)', default='', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', default='', blank=True)
    avatar = models.ImageField(verbose_name='Сменить изображение', upload_to=get_timestamp_path)
    flat = models.ForeignKey('Flat', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'flat_owner'
