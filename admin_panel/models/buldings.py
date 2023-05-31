from django.core import validators
from django.db import models
from .accounts import *
from .website import *

class House(models.Model):
    title = models.CharField(verbose_name='Дом', max_length=100, default='', blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=100, default='', blank=True)
    gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ManyToManyField('HouseUser')

    class Meta:
        db_table = 'house'



class Flat(models.Model):
    number = models.CharField(verbose_name='Номер квартиры', max_length=100, default='', blank=True)
    square = models.PositiveSmallIntegerField(verbose_name='Площадь (кв.м.)', default=0, blank=True)
    house = models.ForeignKey("House", on_delete=models.SET_NULL, null=True, blank=True)
    tariff = models.ForeignKey('TariffSystem', on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)
    floor = models.ForeignKey('Floor', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'flat'


class Section(models.Model):
    title = models.CharField(verbose_name='Секция', max_length=100, default='', blank=True)
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'section'


class Floor(models.Model):
    title = models.CharField(verbose_name='Этаж', max_length=100, default='', blank=True)
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'floor'

