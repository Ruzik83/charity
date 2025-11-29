from django.contrib import admin
from .models import HelpRequest

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'is_approved', 'created_at', 'image')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('full_name', 'phone', 'description')
