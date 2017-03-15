from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    #url(r'^$', views.index ),
    url(r'^$', indexlist.as_view() ),
    url(r'^zakaz_add/$', zakaz_add),
    url(r'^zakaz_detail/(?P<id>\d+)/$', zakaz_detail),
    url(r'^company_zakaz/$', company_zakaz),
]