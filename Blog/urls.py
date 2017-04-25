from django.conf.urls import url, include
from .views import BlogView, BlogList, BlogDetail

app_name = 'Blog'
urlpatterns = [
    url(r'^test/$', BlogView.as_view(), name='blog-view'),
    url(r'^$', BlogList.as_view(), name = 'blog-list'),
    url(r'^detail/(?P<pk>\d+)/$', BlogDetail.as_view(), name = 'blog-detail')

]