# Generated by Django 4.2.1 on 2023-06-26 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_receipt_tariff_alter_receipt_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffservice',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.service', verbose_name='Услуга'),
        ),
    ]
