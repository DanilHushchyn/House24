# Generated by Django 4.2.1 on 2023-06-13 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0023_alter_houseuser_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='houseuser',
            unique_together=set(),
        ),
    ]
