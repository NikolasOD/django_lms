from django import forms

from django_filters import FilterSet

from .models import Student


class BaseStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        value = value.capitalize()
        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        value = value.capitalize()
        return value

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        clear_value = ''
        valid_symbols = ['-', '(', ')']
        for ch in value:
            if ch.isnumeric() or ch in valid_symbols:
                clear_value += ch
        return clear_value


class CreateStudentForm(BaseStudentForm):
    class Meta(BaseStudentForm.Meta):
        pass


class UpdateStudentForm(BaseStudentForm):
    class Meta(BaseStudentForm.Meta):
        exclude = [
            'email'
        ]


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
