import django.forms as forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from ..models import *

User = get_user_model()


class PersonalSignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=Personal.ROLE_CHOICE, label='Роль')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}), label='Email (логин)')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password1'}),
                                label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password2'}),
                                label='Повторить Пароль')
    phone = forms.CharField(max_length=19, label='Номер телефона',
                            validators=[
                                validators.MaxLengthValidator(19),
                                validators.MinLengthValidator(19),
                                validators.ProhibitNullCharactersValidator(),
                                validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                          message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                            ],
                            widget=forms.TextInput(attrs={'placeholder': ''})
                            )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Фамилия')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'status')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        Personal.objects.create(user=user, role=self.cleaned_data.get('role'))
        return user


class PersonalUpdateForm(UserChangeForm):
    role = forms.ChoiceField(choices=Personal.ROLE_CHOICE, label='Роль')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}), label='Email (логин)')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password1'}),
                                label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password2'}),
                                label='Повторить Пароль')
    phone = forms.CharField(max_length=19, label='Номер телефона',
                            validators=[
                                validators.MaxLengthValidator(19),
                                validators.MinLengthValidator(19),
                                validators.ProhibitNullCharactersValidator(),
                                validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                          message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                            ],
                            widget=forms.TextInput(attrs={'placeholder': ''})
                            )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Фамилия')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'status')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        obj = Personal.objects.get(user=user)
        obj.role = self.cleaned_data.get('role')
        obj.save()
        return user


class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}), label='Email (логин)')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password1'}),
                                label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password2'}),
                                label='Повторить Пароль')
    ID = forms.CharField(max_length=11, label='ID', widget=forms.TextInput(attrs={'placeholder': ''}))

    phone = forms.CharField(max_length=19, label='Номер телефона',
                            validators=[
                                validators.MaxLengthValidator(19),
                                validators.MinLengthValidator(19),
                                validators.ProhibitNullCharactersValidator(),
                                validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                          message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                            ],
                            widget=forms.TextInput(attrs={'placeholder': ''})
                            )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Имя')
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Отчество')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Фамилия')
    viber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Viber')
    telegram = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Telegram')

    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ''}), label='О владельце (заметки)')
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '', 'class': 'birthday'}),
                               label='Дата рождения')
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'avatar d-block'}), label='Сменить изображение')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'status')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        FlatOwner.objects.create(user=user, ID=self.cleaned_data.get('ID'),
                                 patronymic=self.cleaned_data.get('patronymic'),
                                 birthday=self.cleaned_data.get('birthday'),
                                 bio=self.cleaned_data.get('bio'), viber=self.cleaned_data.get('viber'),
                                 telegram=self.cleaned_data.get('telegram'))
        return user


class ClientUpdateForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}), label='Email (логин)')
    ID = forms.CharField(max_length=11, label='ID', widget=forms.TextInput(attrs={'placeholder': ''}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password1'}),
                                label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'password2'}),
                                label='Повторить Пароль')
    phone = forms.CharField(max_length=19, label='Номер телефона',
                            validators=[
                                validators.MaxLengthValidator(19),
                                validators.MinLengthValidator(19),
                                validators.ProhibitNullCharactersValidator(),
                                validators.RegexValidator('^\+38 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$',
                                                          message='Неверно введён номер телефона.Пример ввода: +38 (098) 567-81-23')
                            ],
                            widget=forms.TextInput(attrs={'placeholder': ''})
                            )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Имя')
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Отчество')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Фамилия')
    viber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Viber')
    telegram = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Telegram')
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'avatar d-block'}), label='Сменить изображение')

    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ''}), label='О владельце (заметки)')
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '', 'class': 'birthday'}),
                               label='Дата рождения')

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'status')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        obj = FlatOwner.objects.get(user=user)
        obj.birthday = self.cleaned_data.get('birthday')
        obj.patronymic = self.cleaned_data.get('patronymic')
        obj.bio = self.cleaned_data.get('bio')
        obj.viber = self.cleaned_data.get('viber')
        obj.telegram = self.cleaned_data.get('telegram')
        obj.ID = self.cleaned_data.get('ID')
        obj.save()
        return user
