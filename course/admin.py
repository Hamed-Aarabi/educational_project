from django.contrib import admin
from .models import Tag, Course, Episode, Comment


@admin.register(Tag)
class Tag_Admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Episode)
class Episode_Admin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Course)
class Course_Admin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    list_display = ('user', 'course','total_likes','total_dislikes','total_heart', 'created_at')
