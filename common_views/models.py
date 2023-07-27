from django.db import models
from account.models import MyUser


class CommentBaseClass(models.Model):
    user = models.ForeignKey(MyUser, related_name='user_comments', verbose_name='کاربر', null=True,
                             on_delete=models.PROTECT)
    email = models.EmailField(verbose_name='ایمیل', null=True)
    # image = models.ImageField(upload_to='comments', null=True)
    text = models.TextField(verbose_name='دیدگاه')
    parent = models.ForeignKey('self', related_name='comment_parent', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='پاسخ به')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser, related_name='comment_likes', editable=False, verbose_name='تعداد لایک')
    dislikes = models.ManyToManyField(MyUser, related_name='comment_dislike', editable=False,
                                      verbose_name='تعداد دیس لایک')
    heart = models.ManyToManyField(MyUser, editable=False, related_name='comment_heart', verbose_name='تعداد علاقه ها')

    def __str__(self):
        return f'{self.user}'

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
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created_at',)

