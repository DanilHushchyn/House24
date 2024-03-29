from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from House24 import settings
from users.views import *
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/', LoginHouse24.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html',
                                                      html_email_template_name='registration/password_reset_email.html'),
         name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
