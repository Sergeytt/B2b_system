from django.db import models

# Create your models here.
class Dostavka(models.Model):
	create_at = models.DateField(auto_now=True)
	data_dostavki = models.DateField(auto_now=False, verbose_name='Дата доставки')
	company =models.CharField(max_length=50, verbose_name='Компания')
	adress = models.TextField(verbose_name='Адрес')
	score = models.CharField(max_length=20, verbose_name='Счет')
	note = models.TextField(verbose_name='Примечание')
	manager = models.CharField(max_length=30, verbose_name='Менеджер')
	is_active = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Доставка'
		verbose_name_plural = 'Доставки'

	def __str__(self):
		return self.company




