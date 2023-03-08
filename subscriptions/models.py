from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils.validators import validate_sku

class Package(models.Model):
    title = models.CharField(_("title"), max_length=50)
    sku = models.CharField(_("stock keeping unit"), max_length=25, db_index=True, validators=[validate_sku])
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"), blank=True, upload_to="packages/")
    is_enable = models.BooleanField(_("is_enable"), default=True)
    price = models.PositiveSmallIntegerField(_("price"))
    duration = models.DurationField(_("duration"))
    created_time = models.DateTimeField(_("created_time"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated_time"), auto_now_add=True)

    class Meta:
        db_table = "packages"