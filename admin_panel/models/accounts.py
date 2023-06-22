from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from .buldings import *
from admin_panel.utilities import get_timestamp_path


class CustomUser(AbstractUser):
    username = None,
    email = models.EmailField(max_length=255, unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    avatar = models.ImageField(verbose_name='Сменить изображение', upload_to=get_timestamp_path, blank=True, null=True)
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

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'


class Personal(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICE = (
        ('director', 'Директор'),
        ('manager', 'Управляющий'),
        ('accountant', 'Бухгалтер'),
        ('electrician', 'Электрик'),
        ('plumber', 'Сантехник'),
    )

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"

    def application_label(self):
        return f"{self.get_role_display()} - {self.user.last_name} {self.user.first_name}"

    role = models.CharField(max_length=50, choices=ROLE_CHOICE, default='director', verbose_name='Роль')

    class Meta:
        db_table = 'personal'


class FlatOwner(models.Model):
    ID = models.CharField(max_length=11, unique=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    patronymic = models.CharField(verbose_name='Отчество', max_length=100, default='', blank=True)
    viber = models.CharField(verbose_name='Viber', max_length=100, default='', blank=True)
    telegram = models.CharField(verbose_name='Telegram', max_length=100, default='', blank=True)
    bio = models.TextField(verbose_name='О владельце (заметки)', default='', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', default='', blank=True)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.patronymic}"

    class Meta:
        db_table = 'flat_owner'
