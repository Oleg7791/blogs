from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator

def post_list(request):
    posts_list = Post.published.all()
    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(posts_list,3)
    page_num = request.GET.get('page',1)
    posts = paginator.get_page(page_num)
    return render(request,
                  'blogik/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post_slug):
    post_obj = get_object_or_404(Post.published,
                          slug = post_slug,
                          publish__year=year,# publish поле из модели, которое содержит полную дату
                          publish__month=month,
                          publish__day=day,
                          ) #ORM запросы в SQL поэтом двойное __ (лукап)

    return render(request,
                  'blogik/post/detail.html',
                  {'post': post_obj})


def who_post(request):
    who = Post.ooo.all()

    return render(request,
                  'blogik/post/list.html',
                  {'posts':who})