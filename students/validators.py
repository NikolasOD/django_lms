from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'<{(args[0].split("@"))[1]}> is invalid domain name.')


def validate_unique_email(student_email):
    from .models import Student
    if Student.objects.filter(email=student_email).exists():
        raise ValidationError(f'Email <{student_email}> already registered.')
