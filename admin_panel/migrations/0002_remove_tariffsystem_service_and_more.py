# Generated by Django 4.2.1 on 2023-06-04 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariffsystem',
            name='service',
        ),
        migrations.AlterField(
            model_name='article',
            name='debit_credit',
            field=models.CharField(choices=[('plus', 'Приход'), ('minus', 'Расход')], default='plus', max_length=100, verbose_name='Приход/расход'),
        ),
        migrations.AlterField(
            model_name='service',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.measure', verbose_name='Ед. изм.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='show_in_indication',
            field=models.BooleanField(default=False, verbose_name='Показывать в счетчиках'),
        ),
        migrations.CreateModel(
            name='TariffService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.service')),
            ],
            options={
                'db_table': 'tariff_service',
            },
        ),
        migrations.AddField(
            model_name='tariffsystem',
            name='tariff_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_panel.tariffservice'),
        ),
    ]
