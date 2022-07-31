from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(all_posts, 3, orphans=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj':page_obj})