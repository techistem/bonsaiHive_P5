from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'reason',
                    'created_at', )
    list_filter = ('created_at', 'owner__username', 'reason')
    search_fields = ('owner', 'reason', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
