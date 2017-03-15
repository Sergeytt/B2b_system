from django.db import models
import datetime

class Zakupki(models.Model):
	create_at = models.DateField(auto_now=True, verbose_name='Дата создания')
	company = models.CharField(max_length=50, verbose_name='Компания')
	score = models.CharField(max_length=40, verbose_name='Счет')
	code = models.CharField(max_length=40, verbose_name='Артикл')
	name = models.CharField(max_length=100, verbose_name='Наименование')
	col = models.IntegerField(verbose_name='Количество')
	price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name='Цена закупки')
	price_sel = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name='Цена продажи')
	manager = models.CharField(max_length=50, verbose_name='Менеджер')
	status = models.CharField(max_length=20, verbose_name='Статус')

	class Meta:
		verbose_name='Закупкf'
		verbose_name_plural='Закупки'

	def __str__(self):
		return self.name
