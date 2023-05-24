from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import DetailView, TemplateView, ListView, View
from .models import Course, Comment
from datetime import datetime, timedelta



class CourseDetailView(View):
    # template_name = 'course/course_detail.html'
    # model = Course
    # context_object_name = 'course'

    def get(self, request, slug):
        course = Course.objects.get(slug__regex=slug)
        allow = False
        if course.student.filter(id=self.request.user.id).exists():
            allow = True
        comments = course.course_comments.filter(reply_to=None)
        paginator = Paginator(comments, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'course/course_detail.html', {'course':course, 'allow':allow,'page_obj':page_obj})

    def post(self, request, slug):

        reply = request.POST.get('reply_id')
        name, email, text = request.POST.get('name'),request.POST.get('email'),request.POST.get('text')
        Comment.objects.create(user=name,reply_to_id=reply, text=text, email=email, course=Course.objects.get(slug__regex=slug))

        return HttpResponseRedirect(reverse('course:detail', args=[slug]))


class CourseListView(ListView):
    template_name = 'course/course_list.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 1


class SearchBoxView(ListView):
    template_name = 'course/course_list.html'
    model = Course
    paginate_by = 1
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = None
        if query:
            object_list = Course.objects.filter(title__icontains=query)
        return object_list


class CoursesFilter(ListView):
    template_name = 'course/course_list.html'
    model = Course
    paginate_by = 10
    context_object_name = 'courses'



    def get_queryset(self):
        queryset = super(CoursesFilter, self).get_queryset()

        price, title = self.request.GET.get('price', None), self.request.GET.get('tag', None)
        time, is_finished = self.request.GET.get('time', None), self.request.GET.get('status', None)

        if price:
            return queryset.filter(is_free__exact=price)
        if title:
            return queryset.filter(title__icontains=title)
        if is_finished:
            return queryset.filter(is_finished__exact=is_finished)
        if time:
            if time == 'new':
                return queryset.filter(created_at__gte=datetime.now() - timedelta(days=2))
            elif time == 'old':
                return queryset.filter(created_at__lte=datetime.now() - timedelta(days=2))
        return queryset


def comment_like(request,slug, pk):

    comment = Comment.objects.get(id=pk)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user.id)
        return JsonResponse({'response':'remove_like'})
    else:
        comment.likes.add(request.user.id)
        if comment.dislikes.filter(id=request.user.id).exists():
            comment.dislikes.remove(request.user.id)
        return JsonResponse({'response': 'like'})


def comment_dislike(request,slug, pk):

    comment = Comment.objects.get(id=pk)
    if comment.dislikes.filter(id=request.user.id).exists():
        comment.dislikes.remove(request.user.id)
        return JsonResponse({'response':'remove_dislike'})
    else:
        comment.dislikes.add(request.user.id)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user.id)
        return JsonResponse({'response': 'dislike'})

def comment_heart(request,slug, pk):

    comment = Comment.objects.get(id=pk)
    if comment.heart.filter(id=request.user.id).exists():
        comment.heart.remove(request.user.id)
        return JsonResponse({'response':'remove_heart'})
    else:
        comment.heart.add(request.user.id)
        return JsonResponse({'response': 'heart'})