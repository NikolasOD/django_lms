from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Group


class TeacherInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = ('teachers_first_name', 'teachers_last_name', 'teachers_salary')
    extra = 0
    readonly_fields = fields

    def teachers_first_name(self, instance):
        return instance.teacher.first_name

    def teachers_last_name(self, instance):
        return instance.teacher.last_name

    def teachers_salary(self, instance):
        return instance.teacher.salary

    teachers_first_name.short_description = 'first name'
    teachers_last_name.short_description = 'last name'
    teachers_salary.short_description = 'salary'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email',)
    extra = 0
    readonly_fields = fields
    # show_change_link = True

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            group_id=int(request.resolver_match.kwargs['object_id'])
        ).select_related('group')

        return queryset

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_start_date', 'group_end_date', 'count_of_students_link')

    def count_of_students_link(self, obj):
        count = obj.students.count()
        url = (
            reverse("admin:students_student_changelist") + '?' + urlencode({'group_id': f'{obj.pk}'})
        )

        return format_html('<a href="{}">{} student(s)</a>', url, count)

    count_of_students_link.short_description = 'Students'

    fields = (
        'group_name',
        ('group_start_date', 'group_end_date'),
        'headman',
        ('create_datetime', 'update_datetime'),
    )

    readonly_fields = ('group_start_date', 'group_end_date', 'create_datetime', 'update_datetime')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        form.base_fields['headman'].widget.can_view_related = False
        form.base_fields['headman'].queryset = obj.students.all()

        return form

    inlines = [TeacherInlineTable, StudentInlineTable, ]
