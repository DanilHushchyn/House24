from django.core import validators
from django.db import models

from admin_panel.utilities import get_timestamp_path


class Gallery(models.Model):
    img = models.ImageField(upload_to=get_timestamp_path)

    class Meta:
        db_table = 'gallery'


class InfoGallery(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Описание", default='', blank=True)
    img = models.ImageField(upload_to=get_timestamp_path)

    class Meta:
        db_table = 'info_gallery'


class Seo(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Описание", default='', blank=True)
    keywords = models.TextField(verbose_name="Ключевые слова", default='', blank=True)

    class Meta:
        db_table = 'seo'


class AboutUs(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Краткий текст", default='', blank=True)
    extra_title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    extra_description = models.TextField(verbose_name="Краткий текст", default='', blank=True)
    director_photo = models.ImageField(upload_to=get_timestamp_path)
    document = models.FileField(upload_to=get_timestamp_path)
    gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE, null=True, blank=True, related_name='gallery')
    extra_gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='extra_gallery')
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'about_us'


class MainPage(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Краткий текст", default='', blank=True)
    gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE, null=True, blank=True)
    info_gallery = models.ForeignKey("InfoGallery", on_delete=models.CASCADE, null=True, blank=True)
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, null=True)
    show_app_links = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_page'


class SeviceSite(models.Model):
    info_gallery = models.ForeignKey("InfoGallery", on_delete=models.CASCADE, null=True, blank=True)
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'service_site'


class TariffSite(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Краткий текст", default='', blank=True)
    info_gallery = models.ForeignKey("InfoGallery", on_delete=models.CASCADE, null=True, blank=True)
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'tarif_site'


class Contacts(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    description = models.TextField(verbose_name="Краткий текст", default='', blank=True)
    full_name = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    location = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    address = models.CharField(verbose_name='Заголовок', max_length=100, default='', blank=True)
    email = models.EmailField(max_length=150, unique=True, verbose_name='Электронная почта',
                              validators=[
                                  validators.EmailValidator(),
                              ]
                              )
    phone = models.CharField(max_length=19, verbose_name='Номер телефона',
                             validators=[
                                 validators.MaxLengthValidator(19),
                                 validators.MinLengthValidator(19),
                                 validators.ProhibitNullCharactersValidator(),
                                 validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                           message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                             ]
                             )
    site_link = models.URLField(verbose_name='', default='',
                                validators=[
                                    validators.URLValidator(
                                        regex='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)',
                                        message='XYZ'),

                                ],
                                )
    coordinate = models.TextField()
    seo = models.OneToOneField('Seo', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'contacts'
