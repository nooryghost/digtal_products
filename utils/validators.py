from django.utils.translation import ugettext_lazy as _

class SKUValidator(RegexValidator):
    regex = "^[a-zA-Z0-9\-\_]{6,25}$"
    message = "SKU must be alphanumeric with 6 to 25 characters"
    code = "invalid_sku"

class Phone_NumberValidator(RegexValidator):
    regex = "^98(9[0-3,9]\d{8}|[1-9]\d{9})"
    message = "Phone_Number validator must be 12 characters like 98xxxxxxxxxx"
    code = "invalid_phone_number"

class BankCardNumberValidator(RegexValidator):
    regex = "^[0-9]{16}$"
    message = _("Enter a valid card number")
    code = "invalid_bank_card_number"

validate_sku = SKUValidator()
validate_bank_card = BankCardNumberValidator()
validate_phone_number = Phone_NumberValidator()