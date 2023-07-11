from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
from users.forms import *


class LoginFlatOwner(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('cabinet_statistic')
