from django.contrib import admin
from .models import ErrorLog

@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user', 'path', 'method', 'error_message', 'status_code')
    search_fields = ('error_message', 'path')
    list_filter = ('resolved', 'created_at')
    ordering = ('-created_at',)