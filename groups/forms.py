from django import forms

from django_filters import FilterSet

from .models import Group


class BaseGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(BaseGroupForm):
    def __init__(self, *args, **kwargs):
        from students.models import Student
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            queryset=Student.objects.select_related('group'),
            required=False
        )

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'headman'
        ]


class UpdateGroupForm(BaseGroupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False
        )
        self.fields['headman_field'].choices.insert(0, (0, '----------'))

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'start_date',
            'headman',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'group_description': ['exact', 'icontains'],
        }
