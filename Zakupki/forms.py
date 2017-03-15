from django import forms 
from .models import Zakupki

class ZakupkiForm(forms.ModelForm):

	class Meta:
		model = Zakupki
		fields = '__all__'
        
