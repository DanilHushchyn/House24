# Generated by Django 4.2.1 on 2023-06-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_alter_aboutus_director_photo_alter_aboutus_gallery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusdocument',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docs/<function get_timestamp_path at 0x7f4cc1c89bd0>', verbose_name='PDF, JPG (макс. размер 20 Mb)'),
        ),
    ]