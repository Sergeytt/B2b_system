from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View, ListView, DetailView
from .models import Blog

class BlogView(View):
    http_method_names = 'get'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(BlogView, self).dispatch(request)
        else:
            return Http404

    def get(self, request):
        self.test = 'Hello World!'
        return HttpResponse(self.test)


class BlogList(ListView):
    template_name = 'blog/blog_view.html'
    model = Blog
    context_object_name = 'blog_list'


class BlogDetail(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog
    context_object_name = 'blog_list'


    def get_object(self, **kwargs):
        print (self.args)
        print (self.kwargs)
        return super(BlogDetail, self).get_object(**kwargs)



