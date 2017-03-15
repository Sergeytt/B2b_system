from django.shortcuts import render, redirect
from .models import Zakupki
from .forms import ZakupkiForm
from django.views.generic import DetailView, ListView

class indexlist(ListView):
	template_name = 'zakaz.html'
	model = Zakupki

	def dispatch(self, request, *args, **kwargs):
		#self.form = ZakupkiNewForm(request.GET)
		#self.form.is_valid()
		self.test_field = request.GET.get('test_field')
		self.search = request.GET.get('search')
		return super(indexlist, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		queryset = Zakupki.objects.all()
		if self.search:
			queryset = queryset.filter(score=self.search)
		if self.test_field:
			queryset = queryset.order_by(self.test_field)
		return queryset

#def index(request):
#	test = Zakupki.objects.all()
#	return render(request, 'index.html', locals())

def zakaz_add(request):
	if request.method == 'POST':
		form = ZakupkiForm(request.POST or None)
		if form.is_valid():
			data = form.cleaned_data
			print (data['name'])
			new_form = form.save()
			return redirect('/')
	else:
		form = ZakupkiForm()	
	return render(request, 'zakaz_add.html', locals())

def zakaz_detail(request, id):
	tovar = Zakupki.objects.get(id=id)
	form = ZakupkiForm(request.POST or None, instance = tovar)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'zakaz_detail.html', locals())

def company_zakaz(self, request):
	print(self.search)
	zakaz = Zakupki.objects.filter(score=self.search)
	return render(request, 'company_zakaz.html', locals())
