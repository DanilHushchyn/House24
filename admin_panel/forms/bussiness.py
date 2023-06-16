import django.forms as forms

from ..models import *


class PersonalAccountForm(forms.ModelForm):
    number = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'number', 'placeholder': ''}))
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция',
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    flat = forms.ModelChoiceField(queryset=Flat.objects.all(), label='Квартира',
                                  widget=forms.Select(attrs={'class': 'form-flat-select'}))

    def __init__(self, *args, **kwargs):
        super(PersonalAccountForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Выберите..."
        self.fields['section'].empty_label = "Выберите..."
        self.fields['flat'].empty_label = "Выберите..."

    class Meta:
        model = PersonalAccount
        fields = '__all__'
        widgets = {
            'house': forms.Select(attrs={'class': 'form-house-select'}),
        }
