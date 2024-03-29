from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView
from common_views.views import *
from django.db.models import Count, Q
from .models import *
from .filters import course_filters
from datetime import datetime
from django.core.paginator import Paginator


class CourseDetailView(View):
    def get(self, request, slug):
        app_name = get_app_name(request)
        course = Course.objects.get(slug__regex=slug)
        allow = False
        if course.student.filter(id=self.request.user.id).exists():
            allow = True
        comments = course.comment_of_courses.filter(parent=None)
        page_obj = comment_paginator(request, comments)
        tutor_date_joined = (datetime.today() - course.tutor.date_joined).days / 365
        suggested_courses = Course.objects.filter(Q(tutor__username=course.tutor.username)).exclude(id=course.id)
        if len(suggested_courses) > 3:
            suggested_courses = suggested_courses[len(suggested_courses) - 3:]
        return render(request, 'course/course_detail.html',
                      {'course': course, 'allow': allow, 'page_obj': page_obj, 'app_name': app_name,
                       'tutor_date_joined': tutor_date_joined, 'suggested_courses': suggested_courses})

    def post(self, request, slug):
        name, email, parent, text = create_comment(request)
        CourseComment.objects.create(user=name, parent_id=parent, text=text, email=email,
                                     course=Course.objects.get(slug__regex=slug))
        return redirect('course:detail', slug)


# This method show all item of Course model \\
class CourseListView(ListView):
    template_name = 'course/course_list.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 1



class SearchBoxView(View):
    def get(self, request):
        query = self.request.GET.get('q')
        if not query:
            return redirect('home')
        courses = Course.objects.filter(title__icontains=query)
        paginator = Paginator(courses, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'course/course_list.html', {'courses': page_obj, 'page_obj': page_obj})


class CoursesFilter(ListView):
    template_name = 'course/course_list.html'
    model = Course
    paginate_by = 1
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super(CoursesFilter, self).get_queryset()
        price, tag = self.request.GET.get('price', None), self.request.GET.get('tag', None)
        time, is_finished = self.request.GET.get('time', None), self.request.GET.get('status', None)
        queryset = course_filters(price, tag, is_finished, time)
        return queryset


# Source code of functions like, dislike and heart is in views.py in common_views app


def comments_like(request, slug, pk):
    comment = CourseComment.objects.get(id=pk)
    comment_like(request, comment)
    return HttpResponse()


def comments_dislike(request, slug, pk):
    comment = CourseComment.objects.get(id=pk)
    comment_dislike(request, comment)
    return HttpResponse()


def comments_heart(request, slug, pk):
    comment = CourseComment.objects.get(id=pk)
    comment_heart(request, comment)
    return HttpResponse()


class CategoryPartialView(TemplateView):
    template_name = 'course/partial_view.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryPartialView, self).get_context_data(**kwargs)
        categories = Category.objects.annotate(
            num_child_category=Count('child_category')).order_by('-num_child_category', )
        context['categories'] = categories
        return context


class CategoryListView(ListView):
    template_name = 'course/course_list.html'
    model = Category
    context_object_name = 'courses'
    paginate_by = 1

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        queryset = Course.objects.filter(category__name__icontains=self.kwargs.get('name'))
        return queryset


class PartialViewResponsive(TemplateView):
    template_name = 'course/partial_view_responsive.html'

    def get_context_data(self, **kwargs):
        context = super(PartialViewResponsive, self).get_context_data(**kwargs)
        categories = Category.objects.annotate(
            num_child_category=Count('child_category')).order_by('-num_child_category', )
        context['categories'] = categories
        return context
