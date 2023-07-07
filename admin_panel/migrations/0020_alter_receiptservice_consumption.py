# Generated by Django 4.2.1 on 2023-07-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0019_alter_receiptservice_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptservice',
            name='consumption',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='Цена'),
        ),
    ]
