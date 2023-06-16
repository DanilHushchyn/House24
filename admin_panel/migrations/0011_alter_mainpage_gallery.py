# Generated by Django 4.2.1 on 2023-06-06 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_gallery_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallmain', to='admin_panel.gallery'),
        ),
    ]
