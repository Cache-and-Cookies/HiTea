from django.contrib import admin
from .models import *


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('date_submitted',)

    list_display = ('first_name', 'get_date_submitted')
    list_filter = ('date_submitted',)

    def get_date_submitted(self, obj):
        return obj.date_submitted

    get_date_submitted.admin_order_field = 'date_submitted'


admin.site.register(Message, MessageAdmin)
