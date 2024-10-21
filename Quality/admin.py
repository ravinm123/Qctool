from django.contrib import admin
from .models import User
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
 
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email","username","role","display_actions"]
    
    def display_actions(self, obj):
        # Reverse function to generate the correct admin URLs
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])

        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            edit_url,
            delete_url
        )

    display_actions.short_description = "Actions"



    list_filter = ["email"]
    fieldsets = (
            (None, {
                'fields': ('email', 'username', 'role')
            }),
     
            ('Permissions', {
                'fields': ('is_active', 'is_admin')
            }),
        )
    def display_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])

        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            edit_url,
            delete_url
        )

    display_actions.short_description = "Actions"

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username","role", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
         queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

# Now register the new UserAdmin...
admin.site.register(User,UserModelAdmin)


