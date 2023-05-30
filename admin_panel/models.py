from django.contrib.auth.models import AbstractUser
from django.db import models

from admin_panel.utilities import get_timestamp_path


class House(models.Model):
    title = models.CharField(verbose_name='Дом', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE)

    class Meta:
        db_table = 'house'


class Gallery(models.Model):
    img = models.ImageField(upload_to=get_timestamp_path)

    class Meta:
        db_table = 'gallery'


class HouseUser(AbstractUser):
    pass