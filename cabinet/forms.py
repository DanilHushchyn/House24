from datetime import datetime
from django.utils import timezone

from django import forms
from django.template.context_processors import request

from admin_panel.forms import FlatChoiceField
from admin_panel.models import Flat, Application


class CreateApplicationForm(forms.ModelForm):
    ROLE_CHOICE = (
        ('', 'Любой специалист'),
        ('director', 'Директор'),
        ('manager', 'Управляющий'),
        ('accountant', 'Бухгалтер'),
        ('electrician', 'Электрик'),
        ('plumber', 'Сантехник'),
    )
    date_published = forms.DateField(label='',
                                     widget=forms.DateInput(attrs={'class': 'publishing-date', 'placeholder': ''}))
    time_published = forms.TimeField(label='',
                                     widget=forms.TimeInput(attrs={'class': 'publishing-time', 'placeholder': ''}))

    flat = FlatChoiceField(queryset=Flat.objects.filter(house__isnull=False), label='Квартира',
                           widget=forms.Select(attrs={'class': 'form-flat-select select2'}))
    user_type = forms.ChoiceField(choices=ROLE_CHOICE, label='Тип мастера', required=False, )
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '', 'rows': 8}), label='Описание')

    def __init__(self, *args, **kwargs):
        super(CreateApplicationForm, self).__init__(*args, **kwargs)
        self.fields['date_published'].initial = timezone.now().date()
        self.fields['time_published'].initial = datetime.now().time()
        self.fields['flat'].empty_label = "Выберите..."

    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['comment', 'status', 'user']
