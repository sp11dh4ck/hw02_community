from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
from .models import Group, Post

User = get_user_model()

page_count_posts = 10


def paginator(request, post_list):
    paginator = Paginator(post_list, page_count_posts)
    return paginator.get_page(request.GET.get('page'))


def index(request):
    posts = Post.objects.select_related('author').all()
    template = 'posts/index.html'
    context = {
        'page_obj': paginator(request, posts),
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).select_related('group').all()
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'page_obj': paginator(request, posts),
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.all().filter(author=author)
    post_count = Post.objects.filter(author=author).count()
    template = 'posts/profile.html'
    context = {
        'author': author,
        'post_count': post_count,
        'page_obj': paginator(request, posts),
    }
    return render(request, template, context)


def post_detail(request, post_id):
    posts = Post.objects.select_related('author').all()
    post = Post.objects.get(id=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    template = 'posts/post_detail.html'
    context = {
        'posts': posts,
        'post_count': post_count,
        'post': post,
    }
    return render(request, template, context)


# @login_required
# def post_create(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         new_post = form.save()
#         return redirect(new_post)
#     template = 'posts/post_create.html'
#     context = {
#         'form': form,
#         'is_edit': False,
#     }
#     return render(request, template, context)

@login_required
def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('posts:profile', username=request.user)
    template = 'posts/post_create.html'
    context = {
        'form': form
    }
    return render(request, template, context)
