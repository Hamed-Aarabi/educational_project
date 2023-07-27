from django.db import models
from account.models import MyUser


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کاربر', related_name='user_orders')
    final_price = models.PositiveIntegerField(verbose_name='مبلغ قابل پرداخت')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE, verbose_name='برای سفارش')
    name = models.CharField(max_length=255, verbose_name='نام دوره')
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='order', verbose_name='تصویر دوره')
    price = models.PositiveIntegerField(verbose_name='مبلغ دوره')

    def __str__(self):
        return f'{self.order}'
