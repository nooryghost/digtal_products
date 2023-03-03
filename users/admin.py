from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Province


class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username__exact", )
    ordering = ("-id", )


admin.site.register(User, UserAdmin)
admin.site.register(Province)
admin.site.unregister(Group)