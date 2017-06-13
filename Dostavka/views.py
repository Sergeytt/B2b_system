from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Dostavka
from .forms import DostavkaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

#def test_list(request):
#	for_list = Dostavka.objects.all()
#	return render(request, 'dostavka.html', locals())
# Create your views here.

class DostavkaList(ListView):
	template_name = 'dostavka_new.html'
	context_object_name = 'dostavka'
	model = Dostavka

	def dispatch(self, request, *args, **kwargs):
#		#self.form = ZakupkiNewForm(request.GET)
#		#self.form.is_valid()
		self.test_field = request.GET.get('test_field')
		self.search = request.GET.get('search')
		return super(DostavkaList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		dostavka = Dostavka.objects.all()
		if self.search:
			dostavka = dostavka.filter(score=self.search)
		if self.test_field:
			dostavka = dostavka.order_by(self.test_field)
		return dostavka

#	def get_queryset(self):
#		dostavka = Dostavka.objects.all()
#		paginator = Paginator(dostavka, 20)
#		page = self.request.GET.get('page')
#		try:
#			if self.search:
#				dostavka = dostavka.filter(score=self.search)
#			if self.test_field:
#				dos = dostavka.order_by(self.test_field)
#			dostavka = paginator.page(page)
#			# If page is not an integer, deliver first page.
#			if self.search:
#				dostavka = dostavka.filter(score=self.search)
#			if self.test_field:
#				dostavka = dostavka.order_by(self.test_field)
#			dostavka = paginator.page(1)
#		except EmptyPage:
#			# If page is out of range (e.g. 9999), deliver last page of results.
#			if self.search:
#				dostavka = dostavka.filter(score=self.search)
#			if self.test_field:
#				dostavka = dostavka.order_by(self.test_field)
#			dostavka = paginator.page(paginator.num_pages)
#		return dostavka

def Dostavka_today(request):
	now = date.today()
	now = now.strftime('%Y-%m-%d')
	dostavka = Dostavka.objects.filter(data_dostavki = now)
	return render(request, 'dostavka_today.html', locals())

def Dostavka_add(request):
	if request.method == 'POST':
		form = DostavkaForm(request.POST or None)
		if form.is_valid():
			new_form = form.save()
			return redirect('../')
	else:
		form = DostavkaForm()
	return render(request, 'dostavka_add.html', locals())

#class DostavkaDetail(DetailView):
#	template_name = 'dostavka_detail.html'
#	model = Dostavka

def DostavkaDetail(request, id):
	info = Dostavka.objects.get(id = id)
	form = DostavkaForm(request.POST or None, instance=info)
	if form.is_valid():
		form.save()
		return redirect("/dostavka")
	return render(request, 'dostavka_detail.html', locals())

#	def dispatch(self, request, *args, **kwargs):
#		dostavka = Dostavka.objects.get(id=id)
#		form = DostavkaForm(request.POST or None, instance=dostavka)
#		if form.is_valid():
#			form.save()
#			return redirect('/')
#		else:
#			form = DostavkaForm()
#		return (form)