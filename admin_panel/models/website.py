from django.db import models

from admin_panel.utilities import get_timestamp_path


class Gallery(models.Model):
    img = models.ImageField(upload_to=get_timestamp_path)

    class Meta:
        db_table = 'gallery'

