from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Dostavka
from .forms import DostavkaForm

#def test_list(request):
#	for_list = Dostavka.objects.all()
#	return render(request, 'dostavka.html', locals())
# Create your views here.

class DostavkaList(ListView):
	template_name = 'dostavka.html'
	model = Dostavka

def Dostavka_add(request):
	if request.method == 'POST':
		form = DostavkaForm(request.POST or None)
		if form.is_valid():
			new_form = form.save()
			return redirect('/dostavka/')
	else:
		form = DostavkaForm()
	return render(request, 'dostavka_add.html', locals())


