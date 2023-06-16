import json
import os

from django import template
from admin_panel.models import *

register = template.Library()


@register.filter
def disabling(value):
    return Service.objects.filter(measure_id=value).exists()
