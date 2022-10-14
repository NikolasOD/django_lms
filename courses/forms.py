from django import forms

from django_filters import FilterSet

from .models import Course


class BaseCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CreateCourseForm(BaseCourseForm):
    class Meta(BaseCourseForm.Meta):
        pass


class UpdateCourseForm(BaseCourseForm):
    class Meta(BaseCourseForm.Meta):
        pass


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact', 'icontains'],
        }
