from django.contrib import admin
from .models import Article, BlogTag, Category, ArticleComment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'article_author', 'category', 'total_views', 'created_at', 'updated_at')


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_likes', 'total_dislikes', 'total_heart', 'created_at')


@admin.register(BlogTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
