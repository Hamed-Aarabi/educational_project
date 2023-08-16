from django.db import models
from account.models import MyUser


class Teacher(models.Model):
    teacher = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    field = models.CharField(max_length=150)

    def __str__(self):
        return self.teacher.username


class SocialMedia(models.Model):
    SOCIAL_MEDIA_CHOICES = (
        ('telegram', 'تلگرام'),
        ('whatsapp', 'واتس اپ'),
        ('github', 'گیت هاب'),
        ('instagram', 'اینستاگرام'),
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_socials')
    social = models.CharField(max_length=100, choices=SOCIAL_MEDIA_CHOICES)

    def __str__(self):
        return f'{self.teacher}'


class TeachRule(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class TeachRequest(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    field = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.fullname
