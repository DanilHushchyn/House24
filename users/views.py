from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
from users.forms import *


class LoginHouse24(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'Неверная почта или пароль')
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            print('hello2')

            login(self.request, user)
            if user.is_staff:
                return redirect('statistic')
            else:
                return redirect('profile')

    def get_success_url(self):
        return reverse_lazy('profile')


# class LoginHouse24(View):
#     template_name = 'users/login.html'
#     form_class = LoginForm
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         print(form.errors)
#         print(form)
#         print(form.is_valid())
#
#         if form.is_valid():
#             print('hello1')
#
#             user = authenticate(
#                 username=form.cleaned_data['email'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 print('hello2')
#
#                 login(request, user)
#                 if user.is_staff():
#                     return redirect('statistic')
#                 else:
#                     return redirect('profile')
#         message = 'Неправильно указана почта или пароль'
#         return render(request, self.template_name, context={'form': form, 'message': message})


class LogoutHouse24(LogoutView):
    success_url = reverse_lazy('main')
