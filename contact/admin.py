from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group


class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'Email', 'Country', 'CreatedAt')
    list_filter = ('CreatedAt',)

    readonly_fields = ('FirstName', 'LastName', 'TelephoneNumber', 'Country', 'Message', 'Email', 'CreatedAt',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = 'Admin dashboard'
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')
