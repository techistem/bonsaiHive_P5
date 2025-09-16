from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'followed', 'created_at')
    list_filter = ('created_at', 'owner__username', 'followed__username')
    search_fields = ('owner__username', 'followed__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
