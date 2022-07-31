from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.http import Http404

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 2

    #since it doesn't handle string in url-- we need to handle 404 errors.
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(PostListView, self).get_context_data(*args, **kwargs)
