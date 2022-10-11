from django import forms

from django_filters import FilterSet

from .models import Student


class CreateStudentForm(forms.ModelForm):
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

    def clean(self):
        pass

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')
        return value

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


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
