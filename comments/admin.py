from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'owner', 'created_at', 'updated_at')
    list_filter = ('created_at', 'owner__username', 'post__title')
    search_fields = ('owner__username', 'post__title', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    actions = ['delete_selected_comments']
