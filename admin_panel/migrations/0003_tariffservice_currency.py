# Generated by Django 4.2.1 on 2023-06-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_remove_tariffsystem_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffservice',
            name='currency',
            field=models.CharField(blank=True, default='грн'),
        ),
    ]