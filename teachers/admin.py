from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'salary')
    list_display_links = list_display
    list_per_page = 15
    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Birthday', {'fields': ('birthday', 'age')}),
        ('Contacts', {'fields': ('email', 'phone')}),
        ('Service info', {'fields': ('specialization', 'salary')}),
    )

    def age(self, instance):
        return f'{instance.get_age()} y.o.'

    readonly_fields = ('age',)
    age.short_description = 'age'


admin.site.register(Teacher, TeacherAdmin)
