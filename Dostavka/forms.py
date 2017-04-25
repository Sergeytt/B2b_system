from django import forms
from django.forms import widgets
from .models import Dostavka


class DostavkaForm(forms.ModelForm):
    class Meta:
        model = Dostavka
        fields = '__all__'
        exclude = ['is_active']

        widgets = {
            'data_dostavki': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'дд.мм.гггг'}),
            'company': widgets.TextInput(attrs={'class': 'form-control'}),
            'adress': widgets.Textarea(attrs={'cols': 45, 'rows': 2, 'class': 'form-control'}),
            'score': widgets.TextInput(attrs={'class': 'form-control'}),
            'note': widgets.Textarea(attrs={'cols': 45, 'rows': 2, 'class': 'form-control'}),
            'manager': widgets.TextInput(attrs={'class': 'form-control'}),

        }


