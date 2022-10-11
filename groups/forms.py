from django import forms

from .models import Group


class BaseGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_end_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(BaseGroupForm):
    class Meta(BaseGroupForm.Meta):
        pass


class UpdateGroupForm(BaseGroupForm):
    class Meta(BaseGroupForm.Meta):
        exclude = [
            'start_date'
        ]
