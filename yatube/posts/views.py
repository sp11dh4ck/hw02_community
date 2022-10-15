from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    number_posts = 10
    posts = Post.objects.select_related('author').all()[:number_posts]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    number_posts = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group) \
        .select_related('group').all()[:number_posts]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
