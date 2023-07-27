from .models import Article
from datetime import datetime, timedelta


def article_filters(a, b):
    if a and b:
        if b == 'newer':
            return Article.objects.filter(tag__name__icontains=a, created_at__gte=datetime.now() - timedelta(days=2))
        elif b == 'older':
            return Article.objects.filter(tag__name__icontains=a, created_at__lte=datetime.now() - timedelta(days=2))

    elif a:
        return Article.objects.filter(tag__name__icontains=a)
    elif b:
        if b == 'newer':
            return Article.objects.filter(created_at__gte=datetime.now() - timedelta(days=2))
        elif b == 'older':
            return Article.objects.filter(created_at__lte=datetime.now() - timedelta(days=2))
