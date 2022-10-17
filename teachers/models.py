from random import randint

from core.models import PersonModel

from django.db import models


class Teacher(PersonModel):
    specialization = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=10_000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(10_000, 100_000)
        obj.save()
