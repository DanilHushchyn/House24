from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from House24 import settings
from users.views import *

urlpatterns = [
    path('login/', LoginHouse24.as_view(), name='login'),
    path('logout/', LogoutHouse24.as_view(), name='logout'),
]
