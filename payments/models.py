from django.db import models
from django.utils.translation import gettext_lazy as _

class GateWay(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"), upload_to="gateways/")
    is_enable = models.BooleanField(_("is_enable"), default=True)

    created_time = models.DateTimeField(_("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated_time"), auto_now_add=True)
    
    class Meta:
        db_table = "gateways"

class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, _("Void")),
        (STATUS_PAID, _("Payed")),
        (STATUS_ERROR, _("Error")),
        (STATUS_CANCELED, _("Canceled")),
        (STATUS_REFUNDED, _("Refunded"))
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID: _("Payment could not be processed"),
        STATUS_PAID: _("Payment successful"),
        STATUS_ERROR: _("Payment has encountered an error, our team will check it"),
        STATUS_CANCELED: _("Payment canceled by user"),
        STATUS_REFUNDED: _("This payment has been refunded")
        
    }