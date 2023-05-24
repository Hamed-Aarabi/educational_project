from django.shortcuts import render
from django.views.generic import TemplateView
from course.models import Course
from datetime import datetime, timedelta

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['newest_courses'] = Course.objects.filter(created_at__gte=datetime.now() - timedelta(days=2))
        return context