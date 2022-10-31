from django.contrib import admin

from .models import Group


class TeacherInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = ('teachers_first_name', 'teachers_last_name', 'teachers_salary')
    extra = 0
    readonly_fields = ('teachers_first_name', 'teachers_last_name', 'teachers_salary')

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

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_start_date', 'group_end_date')

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

        return form

    inlines = [TeacherInlineTable, StudentInlineTable, ]
