from django.core import validators
from django.db import models
from .accounts import *
from .website import *
from .buldings import *
from admin_panel.utilities import get_timestamp_path


class TariffSystem(models.Model):
    title = models.CharField(verbose_name='Название тарифа', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Описание тарифа", default='', blank=True)
    date_edited = models.DateTimeField(auto_now=True)
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'tariff_system'


class Service(models.Model):
    title = models.CharField(verbose_name='Услуга', max_length=100, default='', blank=True)
    show_in_indication = models.BooleanField(default=False)
    measure = models.ForeignKey('Measure', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'service'


class Measure(models.Model):
    title = models.CharField(verbose_name='Ед. изм.', max_length=100, default='', blank=True)

    class Meta:
        db_table = 'measure'


class PaymentDetail(models.Model):
    title = models.CharField(verbose_name='Название компании', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name='Информация', default='', blank=True)

    class Meta:
        db_table = 'payment_detail'



class Article(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='', blank=True)
    PLUS_MINUS = (
        ('plus', 'Приход'),
        ('minus', 'Расход'),
    )
    debit_credit = models.CharField(verbose_name='Приход/расход', choices=PLUS_MINUS, max_length=100, default='plus',
                                    blank=True)

    class Meta:
        db_table = 'article'


class PersonalAccount(models.Model):
    number = models.CharField(verbose_name='№', max_length=100, default='', blank=True)
    STATUS_CHOICE = (
        ('active', 'Активен'),
        ('disabled', 'Не активен'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='active', verbose_name='Статус')
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True, blank=True)
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True, blank=True)
    flat = models.OneToOneField('Flat', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'personal_account'


class Paybox(models.Model):
    number = models.CharField(verbose_name='', max_length=100, default='', blank=True)
    comment = models.TextField(verbose_name="Комментарий", default='', blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=20)
    flat_owner = models.ForeignKey('FlatOwner', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey("Article", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('HouseUser', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'paybox'


class Receipt(models.Model):
    number = models.CharField(verbose_name='', max_length=100, default='', blank=True)
    is_complete = models.BooleanField(default=True, )
    date_published = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICE = (
        ('paid', 'Оплачена'),
        ('partially_paid', 'Частично оплачена'),
        ('unpaid', 'Не оплачена'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='unpaid', verbose_name='Статус')
    start_date = models.DateField()
    end_date = models.DateField()
    service = models.ManyToManyField('Service', blank=True)
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE)
    total_price = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=20)

    class Meta:
        db_table = 'receipt'


class Indication(models.Model):
    number = models.CharField(verbose_name='', max_length=100, default='', blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICE = (
        ('new', 'Новое'),
        ('considered', 'Учтено'),
        ('considered and paid', 'Учтено и оплачено'),
        ('null', 'Нулевое'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='new', verbose_name='Статус')
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Счётчик')
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира')

    class Meta:
        db_table = 'indication'


class Application(models.Model):
    date_published = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(verbose_name="Комментарий", default='', blank=True)
    description = models.TextField(verbose_name="Описание", default='', blank=True)
    time_published = models.TimeField(auto_now_add=True)
    STATUS_CHOICE = (
        ('new', 'Новое'),
        ('in work', 'В работе'),
        ('complete', 'Выполнено'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='new', verbose_name='Статус')
    user = models.ForeignKey('HouseUser', on_delete=models.SET_NULL, null=True)
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира')
    flat_owner = models.ForeignKey('FlatOwner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'application'


class Message(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(default='', blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('HouseUser', on_delete=models.CASCADE, null=True)
    flat_owner = models.ManyToManyField('FlatOwner')

    class Meta:
        db_table = 'message'