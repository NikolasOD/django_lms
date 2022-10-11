from datetime import date

from core.validators import ValidEmailDomain

from dateutil.relativedelta import relativedelta

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group

from .validators import validate_unique_email

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        db_column='first_name_column',
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        db_column='last_name_column',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[validate_unique_email, ValidEmailDomain(*VALID_DOMAIN_LIST)])
    phone = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(6)],
        error_messages={'min_length': '"phone" field value less than six symbols'}
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='students')
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        for _ in range(cnt):
            f = Faker()
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            f = Faker('uk_UA')
            phone = f.phone_number()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email, phone=phone)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print('Incorrect data.')
