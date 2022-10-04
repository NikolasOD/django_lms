from django import forms

from .models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
        }
