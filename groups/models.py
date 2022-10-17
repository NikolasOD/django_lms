from datetime import date

from core.models import BaseModel

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from teachers.models import Teacher

from .validators import validate_start_date


class Group(BaseModel):
    group_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"group_name" field value less than two symbols'}
    )
    group_start_date = models.DateField(validators=[validate_start_date], default=date.today)
    group_end_date = models.DateField(validators=[validate_start_date], default=date.today, null=True, blank=True)
    group_description = models.TextField(
        max_length=120,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"group_description" field value less than two symbols'},
        null=True,
        blank=True
    )
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='groups'
    )

    def __str__(self):
        return f'Group name: <{self.group_name}>; Start at: <{self.group_start_date}>'

    class Meta:
        db_table = 'groups'

    @classmethod
    def gen_group(cls):
        f = Faker()
        lst = [
            'Python',
            'Java',
            'PM',
            'DevOps',
            'Frontend',
            'QA'
        ]

        for group in lst:
            Group.objects.create(
                group_name=group,
                group_start_date=f.date_between(start_date='today', end_date='+1y'),
            )
