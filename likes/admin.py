from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at')
    list_filter = ('created_at', 'owner__username', 'post__title')
    search_fields = ('owner__username', 'post__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
