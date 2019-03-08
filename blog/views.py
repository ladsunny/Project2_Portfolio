from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def myblog(request):
    blogobjects = Blog.objects.all().order_by('-pub_date')
    return render(request, 'blog/myblog.html', {'blogobjects':blogobjects})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detailblog':detailblog})
