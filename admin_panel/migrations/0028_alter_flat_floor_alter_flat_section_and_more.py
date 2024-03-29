# Generated by Django 4.2.1 on 2023-07-21 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0027_alter_role_application_alter_role_flat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.floor', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.section', verbose_name='Секция'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.house'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='section',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.house'),
        ),
    ]
