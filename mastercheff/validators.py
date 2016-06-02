from django.core.exceptions import ValidationError

from datetime import datetime


def fecha_futura(fehca):
    if fecha > datetime.now:
        raise ValidationError(
            "Fecha invalida, valor futuro"
        )