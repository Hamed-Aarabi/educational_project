from django.db import models
from django.utils.text import slugify
from account.models import MyUser


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
    student = models.ManyToManyField(MyUser, null=True, blank=True, related_name='student_courses')
    tutor = models.ForeignKey(MyUser, null=True, blank=True, related_name='tutor_courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course', verbose_name='تصویر دوره')
    level = models.CharField(max_length=255, verbose_name='سطح دوره')
    price = models.CharField(max_length=255, verbose_name='قیمت دوره')
    course_status = models.CharField(max_length=255, verbose_name='وضعیت دوره')
    slug = models.SlugField(blank=True, allow_unicode=True, unique=True)
    tag = models.ManyToManyField(Tag, verbose_name='برچسب ها')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_free = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Course, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField(verbose_name='کامنت')
    user = models.CharField(verbose_name='کابر', max_length=255)
    email = models.EmailField(verbose_name='ایمیل', null=True)
    course = models.ForeignKey(Course, related_name='course_comments', on_delete=models.CASCADE, verbose_name='دوره')
    reply_to = models.ForeignKey('self', related_name='comment_replys', on_delete=models.CASCADE,blank=True,null=True, verbose_name='پاسخ به')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser, related_name='comment_likes',editable=False, verbose_name='تعداد لایک')
    dislikes = models.ManyToManyField(MyUser, related_name='comment_dislikes',editable=False, verbose_name='تعداد دیس لایک')
    heart = models.ManyToManyField(MyUser, related_name='comment_hearts',editable=False, verbose_name='تعداد قلب ها')

    def __str__(self):
        return self.user

    def total_likes(self):
        return self.likes.count()
    total_likes.short_description = 'تعداد لایک ها'

    def total_dislikes(self):
        return self.dislikes.count()
    total_dislikes.short_description = 'تعداد دیس لایک ها'

    def total_heart(self):
        return self.heart.count()
    total_heart.short_description = 'تعداد قلب ها'


    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural= 'کامنت ها'
        ordering = ('-created_at',)