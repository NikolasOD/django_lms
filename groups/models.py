from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"group_name" field value less than two symbols'}
    )
    group_start_date = models.DateField(validators=[validate_start_date], default=date.today, null=True, blank=True)
    group_description = models.TextField(
        max_length=120,
        verbose_name='group description',
        db_column='group_description',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"group_description" field value less than two symbols'}
    )

    def __str__(self):
        return f'{self.group_name} {self.group_start_date}'

    class Meta:
        db_table = 'groups'

    @classmethod
    def generate_fake_data(cls, cnt):
        for _ in range(cnt):
            f = Faker()
            group_name = f.job()
            group_start_date = f.date_between(start_date='today', end_date='+1y')
            group_description = f.bs()
            gp = cls(group_name=group_name, group_start_date=group_start_date, group_description=group_description)
            try:
                gp.full_clean()
                gp.save()
            except ValidationError:
                print('Incorrect data.')
