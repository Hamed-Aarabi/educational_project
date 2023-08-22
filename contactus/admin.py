from django.contrib import admin
from .models import *


@admin.register(Contactus)
class ContacusAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject')


@admin.register(Counsel)
class CounselAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'status')


admin.site.register(Way)
admin.site.register(ContactWay)
admin.site.register(ContactSocial)
