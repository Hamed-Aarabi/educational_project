from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import MyUser, Ticket



class TicketFilterByStatus(admin.SimpleListFilter):
    parameter_name = 'status'
    title = 'پاسخ'

    def lookups(self, request, model_admin):
        return (
            ('True', 'حل شده'),
            ('False', 'حل نشده')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'status', 'created_at')
    list_filter = (TicketFilterByStatus,)



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["phone", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone"]}),
        ("Personal info", {"fields": ['email', 'username', 'first_name', 'last_name', 'sex', 'image']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
