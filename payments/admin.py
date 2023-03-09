from django.contrib import admin

from .models import GateWay, Payment

@admin.register(GateWay)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ["title", "is_enable"]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "gateway", "price", "status", "phone_number", "created_time"]
    list_filter = ["status", "gateways", "packages"]
    search_fields = ["user__username", "phone_number"]