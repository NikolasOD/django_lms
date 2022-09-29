from django import forms

from .models import Teacher


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
