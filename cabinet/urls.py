from django.urls import path

import cabinet.views

urlpatterns = [
    path("statistic", cabinet.views.statistic, name='cabinet_statistic'),
    path("profile", cabinet.views.profile, name='profile'),


]
