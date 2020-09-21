from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import DetailMixin, CreateMixin, UpdateMixin, DeleteMixin


def blog_list(request):
    """ Представление постов """
    search_post = request.GET.get('search', '')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(context__icontains=search_post))
        search = f'search={ request.GET.get("search") }&'
    else:
        posts = Post.objects.all()
        search = None

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'search':search})


class PostDetail(DetailMixin, View):
    """ Представление поста """
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, CreateMixin, View):
    """ Представления формы создания поста """
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, UpdateMixin, View):
    """ Представление формы обновления поста """
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, DeleteMixin, View):
    """ Представление формы удаления поста """
    model = Post
    template = 'blog/post_delete.html'
    good_luck_address = 'post_list_url'
    raise_exception = True


def tag_list(request):
    """ Представление тегов """
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags':tags})


class TagDetail(DetailMixin, View):
    """ Представление тега """
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, CreateMixin, View):
    """ Представление формы создания тега """
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, UpdateMixin, View):
    """ Представление формы обновления тега """
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, DeleteMixin, View):
    """ Представление формы удаления поста """
    model = Tag
    template = 'blog/tag_delete.html'
    good_luck_address = 'tag_list_url'
    raise_exception = True
