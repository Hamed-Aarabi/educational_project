from django.contrib import admin
from .models import Contactus



@admin.register(Contactus)
class ContacusAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject')


