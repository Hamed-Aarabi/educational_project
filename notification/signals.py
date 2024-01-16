from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from course.models import Course, Episode
from .models import *


@receiver(post_save, sender=Course)
def notify_user(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(title=instance, text=f'دوره {instance} اضافه شد.')


@receiver(pre_save, sender=Episode)
def notify_user_episode(sender, instance, **kwargs):
    Notification.objects.create(title=instance.course, text=f'قسمت جدید برای دوره {instance.course} اضافه شد.')


# @receiver(pre_save, sender=Course)
# def notify_user_discount(sender, instance, **kwargs):
#     if instance.id:
#         old = Course.objects.get(id=instance.id)
#         if old.is_discount != instance.is_discount:
#             DiscountNotification.objects.create(title=instance,
#                                                 text=f'تخفیف {instance.discount_percentage} درصدی برای دوره {instance} اعمال شد.',
#                                                 discount=True)
#         else:
#             if DiscountNotification.objects.filter(title=instance).exists():
#                 course = DiscountNotification.objects.get(title=instance)
#                 course.discount = False
#                 course.save()
