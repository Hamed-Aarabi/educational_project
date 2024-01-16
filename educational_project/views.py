from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from account.models import MyUser
from contactus.forms import CounselForm
from contactus.models import Counsel
from course.models import Course
from datetime import datetime, timedelta
from blog.models import Article


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['newest_courses'] = Course.objects.filter(created_at__gte=datetime.now() - timedelta(days=2))
        context['random_articles'] = Article.objects.order_by('?')[:3]
        context['special_offers'] = Course.objects.filter(Q(is_discount=True) | Q(is_free=True))
        context['form'] = CounselForm
        context['course_count'] = Course.objects.all().count()
        context['user_count'] = MyUser.objects.all().count()
        return context

    def post(self, request):
        form = CounselForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Counsel.objects.create(**cd)
        return JsonResponse({'status': 'success'})


def error_404_view(request, exception):
    return render(request, '404.html')
