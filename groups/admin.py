from django.contrib import admin

from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_start_date', 'headman_name')
    list_display_links = list_display
    list_per_page = 15
    fieldsets = (
        (None, {'fields': ('group_name',)}),
        ('Dates', {'fields': ('group_start_date', 'group_end_date')}),
        ('Relations', {'fields': ('headman', 'teachers')}),
        ('Group description', {'fields': ('group_description',), 'classes': ('collapse',)}),
    )

    def headman_name(self, instance):
        if instance.headman:
            return f'{instance.headman.first_name} {instance.headman.last_name}'
        return ''

    headman_name.short_description = 'headman'


admin.site.register(Group, GroupAdmin)
