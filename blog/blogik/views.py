from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    y = Post.published.all()
    return render(request,
                  'blogik/post/list.html',
                  {'posts': y})

def post_detail(request, year, month, day, post_slug):
    x = get_object_or_404(Post.published,
                          slug = post_slug,
                          publish__year=year,
                          publish__month=month,
                          publish__day=day,
                          ) #ORM запросы в SQL поэтом двойное __ (лукап)

    return render(request,
                  'blogik/post/detail.html',
                  {'post': x})
