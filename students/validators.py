from django.core.exceptions import ValidationError


def validate_unique_email(student_email):
    from .models import Student
    if Student.objects.filter(email=student_email).exists():
        raise ValidationError(f'Email <{student_email}> already registered.')
