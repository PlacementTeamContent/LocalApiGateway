from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created_at', 'active')
    search_fields = ('user', 'key')  # Searchable fields
    list_filter = ('created_at', 'active', 'user')  # Filter options
    ordering = ('user','-created_at')  # Ordering of records
    readonly_fields = ('created_at', 'key', 'user')  # Fields that should not be editable in the admin interface


@admin.register(models.TokenUsage)
class TokenUsageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'input_tokens', 'output_tokens', 'api_key')
    search_fields = ('api_key',)  # Searchable fields
    list_filter = ('timestamp', 'api_key')  # Filter options
    ordering = ('-timestamp',)  # Ordering of records
