# Generated by Django 4.2.1 on 2023-07-09 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0022_alter_flat_number_alter_flat_square'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.house', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='flatowner',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='indication',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.service', verbose_name='Счётчик'),
        ),
    ]
