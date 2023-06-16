import django.forms as forms
from django.forms import modelformset_factory

from ..models import *


class HouseForm(forms.ModelForm):
    title = forms.CharField(label='Название', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': ''}))
    address = forms.CharField(label='Адрес', max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = House
        fields = ('title', 'address')


class HouseUserForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Personal.objects.all(), label='ФИО',
                                  widget=forms.Select(attrs={'class': 'form-role-select'}))

    # def __init__(self, *args, **kwargs):
    #     super(HouseUserForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].empty_label = "Выберите..."

    class Meta:
        model = HouseUser
        fields = ('user',)


HouseUserFormset = forms.modelformset_factory(model=HouseUser, form=HouseUserForm, can_delete=True, extra=0)


class SectionForm(forms.ModelForm):
    title = forms.CharField(label='Название', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = Section
        fields = ('title',)


SectionFormset = forms.modelformset_factory(model=Section, form=SectionForm, can_delete=True, extra=0)


class FloorForm(forms.ModelForm):
    title = forms.CharField(label='Название', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = Floor
        fields = ('title',)


FloorFormset = forms.modelformset_factory(model=Floor, form=FloorForm, can_delete=True, extra=0)


class FlatForm(forms.ModelForm):
    square = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': ''}), label='Площадь')
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label='Секция',
                                     widget=forms.Select(attrs={'class': 'form-section-select'}))
    floor = forms.ModelChoiceField(queryset=Floor.objects.all(), label='Этаж',
                                   widget=forms.Select(attrs={'class': 'form-floor-select'}))

    def __init__(self, *args, **kwargs):
        super(FlatForm, self).__init__(*args, **kwargs)
        self.fields['house'].empty_label = "Выберите..."
        self.fields['section'].empty_label = "Выберите..."
        self.fields['floor'].empty_label = "Выберите..."
        self.fields['flat_owner'].empty_label = "Выберите..."
        self.fields['tariff'].empty_label = "Выберите..."

    class Meta:
        model = Flat
        fields = '__all__'
        widgets = {
            'number': forms.TextInput(attrs={'placeholder': ''}),
            'house': forms.Select(attrs={'class': 'form-house-select'}),
        }


