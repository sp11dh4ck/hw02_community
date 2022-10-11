from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    number_posts = 10
    posts = Post.objects.order_by('-pub_date')[:number_posts]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    number_posts = 10
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:number_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
