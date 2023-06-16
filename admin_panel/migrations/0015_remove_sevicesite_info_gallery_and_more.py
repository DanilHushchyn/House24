# Generated by Django 4.2.1 on 2023-06-07 08:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_alter_aboutusdocument_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sevicesite',
            name='info_gallery',
        ),
        migrations.RemoveField(
            model_name='tariffsite',
            name='info_gallery',
        ),
        migrations.AddField(
            model_name='sevicesite',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='gallery_service', to='admin_panel.gallery'),
        ),
        migrations.AddField(
            model_name='tariffsite',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='gallery_tariff', to='admin_panel.gallery'),
        ),
        migrations.AlterField(
            model_name='aboutusdocument',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docs', verbose_name='PDF, JPG (макс. размер 20 Mb)'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='coordinate',
            field=models.TextField(verbose_name='Код карты'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='location',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=19, validators=[django.core.validators.MaxLengthValidator(19), django.core.validators.MinLengthValidator(19), django.core.validators.ProhibitNullCharactersValidator(), django.core.validators.RegexValidator('^\\+38 \\(\\d{3}\\) \\d{3}-?\\d{2}-?\\d{2}$', message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='site_link',
            field=models.URLField(default='', validators=[django.core.validators.URLValidator(message='XYZ', regex='https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)')], verbose_name='Ссылка на коммерческий сайт'),
        ),
    ]
