# Generated by Django 4.2.1 on 2023-06-05 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_tariffservice_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariffsystem',
            name='tariff_service',
        ),
        migrations.AddField(
            model_name='tariffservice',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.tariffsystem'),
        ),
    ]