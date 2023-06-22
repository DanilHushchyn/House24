import django.forms as forms
from django.db.models import Q
from django.utils import timezone
from datetime import datetime

from ..models import *


class PersonalAccountForm(forms.ModelForm):
    number = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class': 'number', 'placeholder': ''}))
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция', required=False,
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    house = forms.ModelChoiceField(queryset=House.objects.all(), label='Дом', required=False,
                                   widget=forms.Select(attrs={'class': 'form-house-select'}))
    flat = forms.ModelChoiceField(queryset=Flat.objects.all(), label='Квартира', required=False,
                                  widget=forms.Select(attrs={'class': 'form-flat-select'}))

    def __init__(self, *args, **kwargs):
        super(PersonalAccountForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Выберите..."
        self.fields['section'].empty_label = "Выберите..."
        self.fields['flat'].empty_label = "Выберите..."

    class Meta:
        model = PersonalAccount
        fields = '__all__'


class IndicationForm(forms.ModelForm):
    number = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class': 'number', 'placeholder': ''}))
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция', required=False,
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    house = forms.ModelChoiceField(queryset=House.objects.all(), label='Дом', required=False,
                                   widget=forms.Select(attrs={'class': 'form-house-select'}))
    service = forms.ModelChoiceField(queryset=Service.objects.filter(show_in_indication=True), label='Счётчик',
                                     required=False,
                                     widget=forms.Select(attrs={'class': 'form-service-select'}))
    flat = forms.ModelChoiceField(queryset=Flat.objects.all(), label='Квартира',
                                  widget=forms.Select(attrs={'class': 'form-flat-select'}))
    date_published = forms.DateField(label='',
                                     widget=forms.DateInput(attrs={'class': 'publishing-date', 'placeholder': ''}))

    def __init__(self, *args, **kwargs):
        super(IndicationForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Выберите..."
        self.fields['section'].empty_label = "Выберите..."
        self.fields['flat'].empty_label = "Выберите..."
        self.fields['service'].empty_label = "Выберите..."
        self.fields['date_published'].initial = timezone.now().date()

    class Meta:
        model = Indication
        fields = '__all__'
        widgets = {
            'indication_val': forms.NumberInput(attrs={'placeholder': ''})
        }


class PersonalChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.application_label()


class FlatChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.application_label()


class ApplicationForm(forms.ModelForm):
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
    flat_owner = forms.ModelChoiceField(queryset=FlatOwner.objects.all(), label='Владелец квартиры ',
                                        widget=forms.Select(attrs={'class': 'form-flat_owner-select select2'}))

    flat = FlatChoiceField(queryset=Flat.objects.filter(house__isnull=False), label='Квартира',
                           widget=forms.Select(attrs={'class': 'form-flat-select select2'}))

    user = PersonalChoiceField(queryset=Personal.objects.all(), label='Мастер',
                               widget=forms.Select(attrs={'class': 'form-master-select'}))

    user_type = forms.ChoiceField(choices=ROLE_CHOICE, label='Тип мастера', )

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Выберите..."
        self.fields['flat'].empty_label = "Выберите..."
        self.fields['flat_owner'].empty_label = "Выберите..."
        self.fields['user'].empty_label = "Выберите..."

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': '', 'rows': 8}),
            'comment': forms.Textarea(attrs={'placeholder': '', 'rows': 8, 'class': 'summernote'})
        }


class CreateApplicationForm(ApplicationForm):
    def __init__(self, *args, **kwargs):
        ApplicationForm.__init__(self, *args, **kwargs)
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Выберите..."
        self.fields['date_published'].initial = timezone.now().date()
        self.fields['time_published'].initial = datetime.now().time()


class MailBoxForm(forms.ModelForm):
    to_debtors = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'to_debtors rounded-0 shadow-none'}),
                                    required=False,
                                    label='Владельцам с задолженностями')
    house = forms.ModelChoiceField(queryset=House.objects.all(), label='ЖК', required=False,
                                   widget=forms.Select(attrs={'class': 'form-house-select'}))
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция', required=False,
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    floor = forms.ModelChoiceField(queryset=Floor.objects.all(), label='Этаж', required=False,
                                   widget=forms.Select(attrs={'class': 'form-floor-select'}))
    flat = forms.ModelChoiceField(queryset=Flat.objects.all(), label='Квартира', required=False,
                                  widget=forms.Select(attrs={'class': 'form-flat-select'}))

    def __init__(self, *args, **kwargs):
        super(MailBoxForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Всем..."
        self.fields['section'].empty_label = "Всем..."
        self.fields['floor'].empty_label = "Всем..."
        self.fields['flat'].empty_label = "Всем..."

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        if instance.pk:
            q = []
            if self.cleaned_data['house']:
                q.append(Q(house=self.cleaned_data['house']))
                if self.cleaned_data['section']:
                    q.append(Q(section=self.cleaned_data['section']))
                if self.cleaned_data['floor']:
                    q.append(Q(floor=self.cleaned_data['floor']))
                if self.cleaned_data['flat']:
                    q.append(Q(id=self.cleaned_data['flat'].id))
                result = Q()
                for item in q:
                    result = result & item
                flats = Flat.objects.filter(result)
                for flat in flats:
                    instance.flat_owners.add(flat.flat_owner)
            else:
                flat_owners = FlatOwner.objects.all()
                for flat_owner in flat_owners:
                    instance.flat_owners.add(flat_owner)
        return instance

    class Meta:
        model = MailBox
        fields = ('title', 'description', 'house', 'section', 'floor', 'flat')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Тема сообщения'}),
            'description': forms.Textarea(attrs={'placeholder': 'Текст сообщения:'})
        }


class ReceiptForm(forms.ModelForm):
    date_published = forms.DateField(label='',
                                     widget=forms.DateInput(attrs={'class': 'publishing-date', 'placeholder': ''}))
    start_date = forms.DateField(label='Период с',
                                 widget=forms.DateInput(attrs={'class': 'start-date', 'placeholder': ''}))
    end_date = forms.DateField(label='Период по',
                               widget=forms.DateInput(attrs={'class': 'end-date', 'placeholder': ''}))
    number = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class': 'number', 'placeholder': ''}))
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция', required=False,
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    house = forms.ModelChoiceField(queryset=House.objects.all(), label='Дом', required=False,
                                   widget=forms.Select(attrs={'class': 'form-house-select'}))
    flat = forms.ModelChoiceField(queryset=Flat.objects.all(), label='Квартира', required=False,
                                  widget=forms.Select(attrs={'class': 'form-flat-select'}))
    tariff = forms.ModelChoiceField(queryset=TariffSystem.objects.all(), label='Тариф',
                                  widget=forms.Select(attrs={'class': 'form-tariff-select'}))
    personal_account = forms.CharField(label='Лицевой счет',
                                       widget=forms.TextInput(attrs={'class': 'personal_account', 'placeholder': ''}))
    is_complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'shadow-none rounded-0'}),
                                     label='Проведена')

    def __init__(self, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Выберите..."
        self.fields['section'].empty_label = "Выберите..."
        self.fields['flat'].empty_label = "Выберите..."
        self.fields['tariff'].empty_label = "Выберите..."
        self.fields['date_published'].initial = timezone.now().date()
        self.fields['start_date'].initial = timezone.now().date()
        self.fields['end_date'].initial = timezone.now().date()

    class Meta:
        model = Receipt
        fields = '__all__'
        exclude = ('service',)
