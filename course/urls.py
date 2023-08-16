from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

app_name = 'course'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='all'),
    path('search/', views.SearchBoxView.as_view(), name='search'),
    path('filter/', views.CoursesFilter.as_view(), name='filter'),
    path('partial-view/', views.CategoryPartialView.as_view(), name='partial_view'),
    path('partial-view-responsive/', views.PartialViewResponsive.as_view(), name='partial_view_responsive'),
    path('category/<str:name>/', views.CategoryListView.as_view(), name='category_list'),
    re_path(r'(?P<slug>[-\w]+)/like_comment/(?P<pk>[-\w]+)', views.comments_like, name='comment_like'),
    re_path(r'(?P<slug>[-\w]+)/dislike_comment/(?P<pk>[-\w]+)', views.comments_dislike, name='comment_dislike'),
    re_path(r'(?P<slug>[-\w]+)/heart_comment/(?P<pk>[-\w]+)', views.comments_heart, name='comment_heart'),
    re_path(r'(?P<slug>[-\w]+)', views.CourseDetailView.as_view(), name='detail'),

]
