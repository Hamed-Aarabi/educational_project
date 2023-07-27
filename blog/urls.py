from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('search', views.SearchBoxArticle.as_view(), name='search'),
    path('filter', views.ArticleFiltersView.as_view(), name='filter'),
    re_path(r'(?P<slug>[-\w]+)/like_comment/(?P<pk>[-\w]+)', views.blog_comments_lke, name='like'),
    re_path(r'(?P<slug>[-\w]+)/dislike_comment/(?P<pk>[-\w]+)', views.blog_comments_dislike, name='dislike'),
    re_path(r'(?P<slug>[-\w]+)/heart_comment/(?P<pk>[-\w]+)', views.blog_comments_heart, name='heart'),
    re_path(r'(?P<slug>[-\w]+)', views.BlogDetailView.as_view(), name='detail'),

]
