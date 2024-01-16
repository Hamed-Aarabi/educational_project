from django.db import models
from django.utils.text import slugify
from account.models import MyUser
from common_views.models import CommentBaseClass


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='دسته بندی')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Episode(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان قسمت', unique=True)
    description = models.TextField(verbose_name='توضیحات قسمت')
    course = models.ForeignKey('Course', related_name='course_episodes', verbose_name='قسمت های دوره',
                               on_delete=models.CASCADE)
    video = models.FileField(upload_to=f'episodes/courses', null=True, verbose_name='ویدئو')
    uploader = models.ForeignKey(MyUser, related_name='tutor_videos', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'قسمت'
        verbose_name_plural = 'قسمت ها'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام برچسب')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان دوره', unique=True)
    description = models.TextField(verbose_name='توضیحات دوره')
    student = models.ManyToManyField(MyUser, blank=True, related_name='student_courses')
    tutor = models.ForeignKey(MyUser, null=True, blank=True, related_name='tutor_courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course', verbose_name='تصویر دوره')
    level = models.CharField(max_length=255, verbose_name='سطح دوره')
    price = models.PositiveIntegerField(verbose_name='قیمت دوره')
    course_status = models.CharField(max_length=255, verbose_name='وضعیت دوره')
    slug = models.SlugField(blank=True, allow_unicode=True, unique=True)
    tag = models.ManyToManyField(Tag, verbose_name='برچسب ها', related_name='tags_of_course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_free = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    discount_percentage = models.PositiveIntegerField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='course_category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        if self.is_discount:
            self.discount_price = self.price - int((self.price * self.discount_percentage) / 100)
        elif not self.is_discount:
            self.discount_price = None
        super(Course, self).save(*args, **kwargs)


class CourseComment(CommentBaseClass):
    course = models.ForeignKey(Course, related_name='comment_of_courses', on_delete=models.CASCADE, verbose_name='دوره')
