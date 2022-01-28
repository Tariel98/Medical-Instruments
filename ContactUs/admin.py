from django.contrib import admin
from . models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'subject']
    list_display = ['username', 'email', 'subject', 'date']
    readonly_fields = ['date']
