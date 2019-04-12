from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validate_registor_no(value):
    "This is check the number of digits in registation number"
    print(value,type(value))
    if len(str(value)) != 10:
        raise ValidationError(_(f'{value} ]::[ Registration Number Must be 10 digits'))
    else:
        return value

def validate_register_content(value):
    "this will check the '01227' is present or not"
    if '01227' not in str(value):
        raise ValidationError(_(f'{value} ]::[ Invalid formatting of Registration Number'))
    else:
        return value