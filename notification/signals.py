from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from course.models import Course
from .models import *


@receiver(post_save, sender=Course)
def notify_user(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(title=instance, text=f'دوره {instance} اضافه شد.')


@receiver(pre_save, sender=Course)
def notify_user_update(sender, instance, **kwargs):
    if instance.id:
        old = Course.objects.get(pk=instance.id)
        if old.price != instance.price:
            Notification.objects.create(title=instance, text=f'قیمت دوره {instance} به روزرسانی شد.')
