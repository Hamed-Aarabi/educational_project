from .models import Course
from datetime import datetime, timedelta


def course_filters(a, b, c, d):
    if a and b and c and d:
        if d == 'new':
            return Course.objects.filter(is_free__exact=a, tag__name__icontains=b, is_finished__exact=c,
                                         created_at__gte=datetime.now() - timedelta(days=2))
        elif d == 'old':
            return Course.objects.filter(is_free__exact=a, tag__name__icontains=b, is_finished__exact=c,
                                         created_at__lte=datetime.now() - timedelta(days=2))
    elif a and b and c:
        return Course.objects.filter(is_free__exact=a, tag__name__icontains=b, is_finished__exact=c)
    elif b and c and d:
        if d == 'new':
            return Course.objects.filter(tag__name__icontains=b, is_finished__exact=c,
                                         created_at__gte=datetime.now() - timedelta(days=2))
        elif d == 'old':
            return Course.objects.filter(tag__name__icontains=b, is_finished__exact=c,
                                         created_at__lte=datetime.now() - timedelta(days=2))
    elif a and b:
        return Course.objects.filter(is_free__exact=a, tag__name__icontains=b)
    elif a and c:
        return Course.objects.filter(is_free__exact=a, is_finished__exact=c)
    elif b and c:
        return Course.objects.filter(tag__name__icontains=b, is_finished__exact=c)
    elif b and d:
        if d == 'new':
            return Course.objects.filter(tag__name__icontains=b,
                                         created_at__gte=datetime.now() - timedelta(days=2))
        elif d == 'old':
            return Course.objects.filter(tag__name__icontains=b,
                                         created_at__lte=datetime.now() - timedelta(days=2))
    elif a and d:
        if d == 'new':
            return Course.objects.filter(is_free__exact=a,
                                         created_at__gte=datetime.now() - timedelta(days=2))
        elif d == 'old':
            return Course.objects.filter(is_free__exact=a,
                                         created_at__lte=datetime.now() - timedelta(days=2))
    elif a:
        return Course.objects.filter(is_free__exact=a)
    elif b:
        return Course.objects.filter(tag__name__icontains=b)
    elif c:
        return Course.objects.filter(is_finished__exact=c)
    elif d:
        if d == 'new':
            return Course.objects.filter(created_at__gte=datetime.now() - timedelta(days=2))
        elif d == 'old':
            return Course.objects.filter(created_at__lte=datetime.now() - timedelta(days=2))
