from django.db import models
from django.utils.text import slugify
from account.models import MyUser
from common_views.models import CommentBaseClass


class BlogTag(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام برچسب')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان مقاله', unique=True)
    image = models.ImageField(upload_to='blogs')
    author = models.ForeignKey(MyUser, related_name='author_articles', on_delete=models.CASCADE,
                               verbose_name='نوسینده مقاله')
    text = models.TextField(verbose_name='متن مقاله')
    category = models.ForeignKey(Category, related_name='category_articles', on_delete=models.CASCADE,
                                 verbose_name='دسته بندی')
    tag = models.ManyToManyField(BlogTag, verbose_name='برچسب')
    views = models.ManyToManyField(MyUser, editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True, unique=True, allow_unicode=True)

    def __str__(self):
        return self.title

    def article_author(self):
        if self.author.full_name():
            return self.author.full_name()
        else:
            return self.author.username

    article_author.short_description = 'نویسنده'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ('-created_at',)

    def total_views(self):
        return self.views.all().count()

    total_views.short_description = 'تعداد بازدید'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Article, self).save()


class ArticleComment(CommentBaseClass):
    article = models.ForeignKey(Article, related_name='comment_of_articles', on_delete=models.CASCADE,
                                verbose_name='مقاله')



