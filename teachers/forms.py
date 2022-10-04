from django import forms

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'specialization',
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


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'specialization',
            'birthday',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
