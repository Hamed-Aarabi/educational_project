from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView


app_name = 'course'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='all' ),
    path('search/', views.SearchBoxView.as_view(), name='search' ),
    path('filter/', views.CoursesFilter.as_view(), name='filter' ),
    re_path(r'(?P<slug>[-\w]+)/like_comment/(?P<pk>[-\w]+)', views.comment_like, name='comment_like'),
    re_path(r'(?P<slug>[-\w]+)/dislike_comment/(?P<pk>[-\w]+)', views.comment_dislike, name='comment_dislike'),
    re_path(r'(?P<slug>[-\w]+)/heart_comment/(?P<pk>[-\w]+)', views.comment_heart, name='comment_heart'),
    re_path(r'(?P<slug>[-\w]+)', views.CourseDetailView.as_view(), name='detail'),


]