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
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True), required=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(BaseGroupForm.Meta):
        pass


class UpdateGroupForm(BaseGroupForm):
    class Meta(BaseGroupForm.Meta):
        exclude = [
            'start_date'
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'group_description': ['exact', 'icontains'],
        }
