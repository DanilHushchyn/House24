# Generated by Django 4.2.1 on 2023-06-27 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_receiptservice_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='paybox',
            name='is_complete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='paybox',
            name='personal_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.personalaccount'),
        ),
        migrations.AddField(
            model_name='personalaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='paybox',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='paybox',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.personal'),
        ),
    ]
