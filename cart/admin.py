from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'final_price', "is_paid", 'created_at')
    inlines = (OrderItemAdmin,)
