from django import forms
from .models import Dostavka

class DostavkaForm(forms.ModelForm):
    class Meta:
        model = Dostavka
        fields = '__all__'

