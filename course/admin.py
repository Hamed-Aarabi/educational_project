from django.contrib import admin
from .models import *


@admin.register(Tag)
class Tag_Admin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Episode)
class Episode_Admin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Course)
class Course_Admin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_likes', 'total_dislikes', 'total_heart', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
