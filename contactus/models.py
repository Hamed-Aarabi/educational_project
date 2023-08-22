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


class Counsel(models.Model):
    fullname = models.CharField(max_length=150, verbose_name='نام و نام خانولدگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'مشاوره'
        verbose_name_plural = 'مشاوره ها'


class Way(models.Model):
    CHOICE_WAY = (
        ('map-marker-alt', 'آدرس'),
        ('envelope', 'ایمیل'),
        ('phone', 'تلفن'),

    )
    name = models.CharField(max_length=100, choices=CHOICE_WAY)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ContactWay(models.Model):
    short_description = models.TextField()
    ways = models.ManyToManyField(Way, related_name='contact_ways')


class ContactSocial(models.Model):
    CHOICE_CONTACT_SOCIAL = (
        ('telegram', 'تلگرام'),
        ('youtube', 'یوتیوب'),
        ('instagram', 'اینستاگرام'),
        ('whatsapp', 'واتس اپ'),
        ('github', 'گیت هاب'),
    )
    name = models.CharField(max_length=100, choices=CHOICE_CONTACT_SOCIAL)
    link = models.URLField()

    def __str__(self):
        return self.name
