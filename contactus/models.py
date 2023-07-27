from django.db import models

from account.models import MyUser


class Contactus(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=255, verbose_name='موضوع')
    text = models.TextField(verbose_name='متن پیام')


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'



