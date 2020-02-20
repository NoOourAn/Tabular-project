from django.contrib import admin
from .models import Timetables

readonly_fields = ('orgId', 'AccessCode', 'exams', 'startDate', 'dueDate',)
change_form_template = 'admin/contact/contact_change_list.html'


class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('orgId', 'accessCode', 'exams', 'startDate', 'dueDate',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Timetables, ServicesAdmin)
