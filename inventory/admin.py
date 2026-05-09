from django.contrib import admin
from .models import Asset, Assignment, ChatHistory

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'asset_model', 'serial_number', 'status', 'created_at')
    list_filter = ('status', 'asset_model')
    search_fields = ('name', 'serial_number', 'asset_model')
    readonly_fields = ('qr_code',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee_name', 'assignment_date', 'return_date')
    list_filter = ('assignment_date',)
    search_fields = ('employee_name', 'asset__name', 'asset__serial_number')

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'timestamp')
    search_fields = ('asset__name', 'user_query')
