from django.core.validators import MinLengthValidator
from django.db import models


class Course(models.Model):
    course_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"course_name" field value less than two symbols'}
    )
    course_duration = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"course_duration" field value less than two symbols'}
    )
    course_price = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"course_price" field value less than two symbols'},
    )
    course_requirements = models.TextField(
        max_length=50,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"course_requirements" field value less than two symbols'},
        null=True,
        blank=True
    )
    group = models.OneToOneField(
        'groups.Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course_group'
    )
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Course name: <{self.course_name}>; Duration: <{self.course_duration}>'

    class Meta:
        db_table = 'courses'
