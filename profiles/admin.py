from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name',
                    'created_at', 'updated_at')
    list_filter = ('created_at', 'owner__username')
    search_fields = ('owner__username', 'name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
