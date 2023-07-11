from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from House24 import settings
from users.views import *

urlpatterns = [
    path('login/', LoginFlatOwner.as_view(), name='login'),
]
