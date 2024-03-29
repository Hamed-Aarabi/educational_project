from django.db import models
from course.models import Course


class Notification(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_notifications')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


# class DiscountNotification(models.Model):
#     title = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_discount_notification', null=True)
#     text = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     discount = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.title}'