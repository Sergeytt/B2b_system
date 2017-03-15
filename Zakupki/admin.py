from django.contrib import admin
from Zakupki.models import Zakupki

class ZakupkiAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Zakupki._meta.fields]

	class Meta:
		model = Zakupki

admin.site.register(Zakupki, ZakupkiAdmin)