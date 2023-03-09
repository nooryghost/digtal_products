from django.utils.translation import ugettext_lazy as _

class SKUValidator(RegexValidator):
    regex = "^[a-zA-Z0-9\-\_]{6,25}$"
    message = "SKU must be alphanumeric with 6 to 25 characters"
    code = "invalid_sku"

class Phone_NumberValidator(RegexValidator):
    regex = ""

validate_sku = SKUValidator()