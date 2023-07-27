from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .filters import article_filters
from blog.models import Article, ArticleComment
from common_views.views import *
from django.db.models import Q


class BlogListView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    paginate_by = 1
    context_object_name = 'articles'


class BlogDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['app_name'] = get_app_name(self.request)
        article = Article.objects.get(slug__regex=self.kwargs.get('slug'))
        comments = article.comment_of_articles.filter(parent=None)
        context['page_obj'] = comment_paginator(self.request, comments)
        suggested_articles = Article.objects.filter(
            Q(category__exact=article.category) | Q(author__username=article.author.username))
        if len(suggested_articles) > 3:
            context['suggested_articles'] = suggested_articles
        return context

    def post(self, request, slug):
        name, email, image, parent, text = create_comment(request)
        ArticleComment.objects.create(article=Article.objects.get(slug__regex=slug), user=name, email=email, text=text,
                                      parent_id=parent, image=image)
        return redirect('blog:detail', slug)


class SearchBoxArticle(ListView):
    template_name = 'blog/article_list.html'
    paginate_by = 1
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = None
        if query:
            object_list = Article.objects.filter(title__icontains=query)
        return object_list


class ArticleFiltersView(ListView):
    template_name = 'blog/article_list.html'
    paginate_by = 1
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        time, cat = self.request.GET.get('time'), self.request.GET.get('tag')
        object_list = article_filters(cat, time)
        return object_list


def blog_comments_lke(request, slug, pk):
    comment = ArticleComment.objects.get(id=pk)
    comment_like(request, comment)
    return HttpResponse()


def blog_comments_dislike(request, slug, pk):
    comment = ArticleComment.objects.get(id=pk)
    comment_dislike(request, comment)
    return HttpResponse()


def blog_comments_heart(request, slug, pk):
    comment = ArticleComment.objects.get(id=pk)
    comment_heart(request, comment)
    return HttpResponse()
