# Generated by Django 4.2.1 on 2023-06-26 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_alter_tariffservice_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptservice',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.receipt'),
        ),
    ]
