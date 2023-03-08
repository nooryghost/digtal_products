from django.contrib import admin

from .models import Package, Subscription

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["title", "sku", "price", "duration"]

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "expire_time", "created_time"]