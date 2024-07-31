from django.contrib import admin
from .models import Contact, Group
from django.contrib import admin
from .models import Contact, Group


class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'dev_type', 'status')
    search_fields = ('fullname', 'phone', 'dev_type')
    list_filter = ('dev_type',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Group)
