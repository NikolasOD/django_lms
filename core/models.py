from datetime import date

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import ValidEmailDomain


class BaseModel(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')

    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"last_name" field value less than two symbols')]
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)], unique=True)
    phone = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(6)],
        error_messages={'min_length': '"phone" field value less than six symbols'}
    )

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        f = Faker('uk_UA')
        phone = f.phone_number()

        f = Faker()
        first_name = f.first_name()
        last_name = f.last_name()

        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-15y'),
            email=f'{first_name}.{last_name}{f.random.choice(cls.VALID_DOMAIN_LIST)}',
            phone=phone
        )

        obj.save()
        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
