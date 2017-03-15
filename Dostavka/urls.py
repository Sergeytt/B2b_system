from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    #url(r'^$', views.index ),
    url(r'^$', DostavkaList.as_view() ),
    url(r'add/$', Dostavka_add),

]