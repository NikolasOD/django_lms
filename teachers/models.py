from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    specialization = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"specialization" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(6)],
        error_messages={'min_length': '"phone" field value less than six symbols'}
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        for _ in range(cnt):
            f = Faker()
            first_name = f.first_name()
            last_name = f.last_name()
            specialization = f.job()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            f = Faker('uk_UA')
            phone = f.phone_number()
            st = cls(first_name=first_name,
                     last_name=last_name,
                     specialization=specialization,
                     birthday=birthday,
                     email=email,
                     phone=phone)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print('Incorrect data.')