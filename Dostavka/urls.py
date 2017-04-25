from django.conf.urls import url, include
from django.contrib import admin
from .views import *

app_name = 'dostavka'

urlpatterns = [
    #url(r'^$', views.index ),
    url(r'^$', DostavkaList.as_view(), name = 'list'),
    url(r'^today/$', Dostavka_today, name = 'today'),
    url(r'^add/$', Dostavka_add, name = 'add'),
    url(r'^detail/(?P<pk>\d+)/$', DostavkaDetail.as_view(), name='detail'),

]