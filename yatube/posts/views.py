from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Group, Post
from django.contrib.auth import get_user_model


User = get_user_model()

page_count_posts = 10


def paginator(request, post_list):
    paginator = Paginator(post_list, page_count_posts)
    return paginator.get_page(request.GET.get('page'))


def index(request):
    posts = Post.objects.select_related('author').all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (Post.objects.filter(group=group).select_related('group').all())
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.all().filter(author=author)
    template = 'posts/profile.html'
    context = {
        'author': author,
        'page_obj': paginator(request, posts),
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # post = get_object_or_404(Post, id=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    template = 'posts/post_detail.html'
    context = {
        'post_count': post_count,
        'post': post,
        'post_id': post_id,
    }
    return render(request, template, context)
