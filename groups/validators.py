from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(group_start_date):
    if group_start_date < date.today():
        raise ValidationError(f'<{group_start_date}> is incorrect date.')
